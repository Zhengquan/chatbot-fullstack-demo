from flask import Flask, request, Response, jsonify, render_template, redirect, g
from flask_cors import CORS
from openai import OpenAI
import json
import logging
from functools import wraps
from urllib.parse import quote

app = Flask(__name__, template_folder='templates')
CORS(app)  # 启用CORS支持

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 加载配置文件
def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_mapped_model(model_id):
    config = load_config()
    models = config.get('models', {})
    if model_id in models:
        return models[model_id].get('api_model', model_id)
    return model_id

def get_model_config(model_id):
    """获取指定模型的配置"""
    config = load_config()
    models = config.get('models', {})
    if model_id in models:
        return models[model_id]
    return None

def load_agent_config():
    try:
        with open('agent_config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 返回默认配置
        default_config = {
            "system_prompt": "你是银行内部的智能办公助手，你需要：\n1. 严格遵守银行业务规范和保密制度\n2. 提供准确、规范的业务咨询和操作指导\n3. 协助完成日常办公文件处理和数据分析\n4. 保持专业、严谨的工作态度\n5. 确保信息安全，不讨论敏感信息",
            
            "user_prompt": "在与我交流时，请：\n1. 严格按照银行规章制度提供服务\n2. 对于超出权限的问题，明确告知无法处理\n3. 需要补充信息时，有条理地提出问题\n4. 保持严谨的专业用语和表达方式",
            
            "assistant_prompt": "作为银行智能助手，我将：\n1. 确保回答的专业性和准确性\n2. 严格遵守信息安全规范\n3. 使用规范的银行业务术语\n4. 保持高效、严谨的服务态度\n5. 在权限范围内提供最大帮助",
            
            "conversation_max_turns": 10,
            "welcome_message": "您好，我是银行智能办公助手。我将严格遵守银行规范，协助您完成工作。"
        }
        # 创建默认配置文件
        with open('agent_config.json', 'w', encoding='utf-8') as f:
            json.dump(default_config, f, ensure_ascii=False, indent=4)
        return default_config

def check_auth(username, password):
    with open('config.json') as f:
        config = json.load(f)
    return username == config['admin']['username'] and password == config['admin']['password']

# 定义需要排除认证的路径（精确匹配）
PUBLIC_PATHS = { }

# 定义需要排除认证的路径前缀
PUBLIC_PREFIXES = (
    '/static',  # 静态资源
)

@app.before_request
def authenticate():
    # 检查精确匹配的公开路径
    if request.path in PUBLIC_PATHS:
        return None
        
    # 检查路径前缀
    if request.path.startswith(PUBLIC_PREFIXES):
        return None
        
    # 检查认证
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        # 对中文进行RFC 5987编码
        auth_realm = 'UTF-8\'\'%s' % quote('管理员登录', safe='')
        return Response(
            '需要认证才能访问此页面\n请使用管理员账号登录', 
            401,
            {'WWW-Authenticate': f'Basic realm="{auth_realm}", charset="UTF-8"'}
        )
    return None

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])
    model = data.get('model', 'deepseek-r1')
    stream = data.get('stream', True)
    
    # 加载agent配置
    agent_config = load_agent_config()
    
    # 构建完整的消息历史
    full_messages = []
    
    # 添加系统提示词
    if agent_config.get('system_prompt'):
        full_messages.append({
            "role": "system",
            "content": agent_config['system_prompt']
        })
    
    # 添加对话记忆
    memory = agent_config.get('conversation_memory', [])
    max_turns = agent_config.get('conversation_max_turns', 10)
    
    # 只保留最近的对话历史
    recent_messages = messages[-max_turns*2:] if len(messages) > max_turns*2 else messages
    full_messages.extend(memory)
    full_messages.extend(recent_messages)
    
    try:
        # 获取模型配置
        model_config = get_model_config(model)
        if not model_config:
            return jsonify({"error": "未找到模型配置"}), 400
            
        # 使用模型特定的配置创建client
        client = OpenAI(
            api_key=model_config['api_key'],
            base_url=model_config['base_url']
        )
        
        # 记录API调用信息（减少日志输出）
        logger.info(f"使用模型 {model_config['name']} 进行对话")

        def generate():
            try:
                response = client.chat.completions.create(
                    model=model_config['api_model'],
                    messages=full_messages,
                    stream=stream
                )

                if stream:
                    for chunk in response:
                        response_data = {}
                        
                        if hasattr(chunk.choices[0].delta, 'reasoning_content'):
                            reasoning = chunk.choices[0].delta.reasoning_content
                            response_data['reasoning_content'] = reasoning
                        
                        if hasattr(chunk.choices[0].delta, 'content'):
                            if chunk.choices[0].delta.content:
                                content = chunk.choices[0].delta.content
                                response_data['content'] = content

                        if response_data:
                            yield f"data: {json.dumps(response_data, ensure_ascii=False)}\n\n"
                else:
                    content = response.choices[0].message.content
                    response_data = {
                        'content': content
                    }
                    yield f"data: {json.dumps(response_data, ensure_ascii=False)}\n\n"

            except Exception as e:
                logger.error(f"API调用错误: {str(e)}", exc_info=True)
                yield f"data: {json.dumps({'error': str(e)}, ensure_ascii=False)}\n\n"

        return Response(generate(), mimetype='text/event-stream')

    except Exception as e:
        logger.error(f"请求处理错误: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

# 企业微信安装完成回调
@app.route('/install/callback', methods=['GET', 'POST'])
def install_callback():
    try:
        if request.method == 'GET':
            # 处理安装验证请求
            return request.args.get('echostr', '')
        else:
            # 处理安装成功回调
            data = request.json
            print("收到安装回调:", data)
            # TODO: 处理安装信息
            return jsonify({"errcode": 0, "errmsg": "ok"})
    except Exception as e:
        print(f"安装回调错误: {str(e)}")
        return jsonify({"errcode": -1, "errmsg": str(e)})

# 业务设置页面
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        # 从agent_config.json获取所有设置
        agent_settings = load_agent_config()
        return render_template('settings.html', agent_settings=agent_settings)
    else:
        try:
            data = request.get_json()
            
            # 更新agent配置
            agent_config = {
                'system_prompt': data.get('system_prompt', ''),
                'user_prompt': data.get('user_prompt', ''),
                'assistant_prompt': data.get('assistant_prompt', ''),
                'conversation_max_turns': int(data.get('conversation_max_turns', 5)),
                'welcome_message': data.get('welcome_message', '你好，我是一个专业、友好的AI助手!')
            }
            with open('agent_config.json', 'w', encoding='utf-8') as f:
                json.dump(agent_config, f, ensure_ascii=False, indent=4)
                
            return jsonify({"errcode": 0, "errmsg": "设置已保存"})
        except Exception as e:
            return jsonify({"errcode": -1, "errmsg": f"保存失败: {str(e)}"})

# 数据回调
@app.route('/data/callback', methods=['POST'])
def data_callback():
    try:
        data = request.json
        print("收到数据回调:", data)
        # TODO: 处理数据回调
        return jsonify({"errcode": 0, "errmsg": "ok"})
    except Exception as e:
        print(f"数据回调错误: {str(e)}")
        return jsonify({"errcode": -1, "errmsg": str(e)})

# 指令回调
@app.route('/command/callback', methods=['POST'])
def command_callback():
    try:
        data = request.json
        print("收到指令回调:", data)
        # TODO: 处理指令回调
        return jsonify({"errcode": 0, "errmsg": "ok"})
    except Exception as e:
        print(f"指令回调错误: {str(e)}")
        return jsonify({"errcode": -1, "errmsg": str(e)})

# 移动端首页
@app.route('/app/home')
def app_home():
    agent_config = load_agent_config()
    welcome_message = agent_config.get('welcome_message', '你好，我是一个专业、友好的AI助手')
    return render_template('home.html', welcome_message=welcome_message)

# 桌面端首页
@app.route('/desktop/home')
def desktop_home():
    agent_config = load_agent_config()
    welcome_message = agent_config.get('welcome_message', '你好，我是一个专业、友好的AI助手')
    return render_template('home.html', welcome_message=welcome_message)

# 默认路由重定向到移动端首页
@app.route('/')
def index():
    return redirect('/app/home')

@app.route('/get_models')
def get_models():
    config = load_config()
    return jsonify(config.get('models', {}))

@app.route('/get_agent_config')
def get_agent_config():
    config = load_agent_config()
    return jsonify({
        'conversation_max_turns': config.get('conversation_max_turns', 5)
    })

# 修改加载历史消息的部分
def load_chat_history(chat_id):
    try:
        # 从本地存储获取会话数据
        sessions = json.loads(request.cookies.get(SESSION_STORAGE_KEY, '[]'))
        session = next((s for s in sessions if s['id'] == chat_id), None)
        
        if not session:
            return []
            
        # 确保消息格式一致
        formatted_messages = []
        for msg in session.get('messages', []):
            if msg['role'] == 'assistant':
                # 如果有思考过程，先添加思考过程
                if msg.get('reasoning'):
                    formatted_messages.append({
                        'role': 'assistant',
                        'content': msg['reasoning'],
                        'format': 'reasoning',
                        'timestamp': msg.get('timestamp', '')
                    })
                # 再添加回答内容
                formatted_messages.append({
                    'role': 'assistant',
                    'content': msg['content'],
                    'format': 'standard',
                    'timestamp': msg.get('timestamp', '')
                })
            else:
                formatted_messages.append({
                    'role': msg['role'],
                    'content': msg['content'],
                    'format': 'standard',
                    'timestamp': msg.get('timestamp', '')
                })
        
        return formatted_messages
        
    except Exception as e:
        logger.error(f"加载会话历史失败: {str(e)}")
        return []

@app.route('/api/select_chat', methods=['POST'])
def select_chat():
    data = request.get_json()
    chat_id = data.get('chat_id')
    
    # 加载并返回会话历史
    history = load_chat_history(chat_id)
    return jsonify({
        'success': True,
        'history': history,
        'chat_id': chat_id
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # 修改端口为5001 