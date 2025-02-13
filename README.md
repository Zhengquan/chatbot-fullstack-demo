# 银行智能办公助手系统

## 项目概述

本系统是为银行内部设计的智能办公助手解决方案，基于大语言模型实现，提供安全、专业的业务咨询和办公协助服务。系统具备完善的权限控制、可配置的业务规则和与企业微信的深度集成能力。

## 功能概览

### 会话管理
![Overview](https://private-user-images.githubusercontent.com/251222/412807057-64817b74-550f-4c01-9077-a889653d1f94.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk0Mzc1MDMsIm5iZiI6MTczOTQzNzIwMywicGF0aCI6Ii8yNTEyMjIvNDEyODA3MDU3LTY0ODE3Yjc0LTU1MGYtNGMwMS05MDc3LWE4ODk2NTNkMWY5NC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxM1QwOTAwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hODg2NDg2N2U3ZWY0NzU2OTRmZDNmODFiYTZhZjM5NmY5MDUwNzdhZTU2YTQ4MDE0NTUwNTk2ZTg1ZjA5YWIxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.OZ9uBCoDLPT-09u8d8PL8szH9Gc2NFkzGQ-6GdKqkEY)


### 思维链支持
![CoT](https://private-user-images.githubusercontent.com/251222/412806710-60e6fb9b-99fb-411e-a537-1c7d56fced39.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk0Mzc1MDMsIm5iZiI6MTczOTQzNzIwMywicGF0aCI6Ii8yNTEyMjIvNDEyODA2NzEwLTYwZTZmYjliLTk5ZmItNDExZS1hNTM3LTFjN2Q1NmZjZWQzOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxM1QwOTAwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02ZWIxMmY4NmYwZTdiMWRlMWYwMmYzYjY2NmViMTYxN2M3ZTM5NmE0YTVhNTY4ZTU2Y2RhYWFlY2QyNmU0M2QzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-jJHLkay3MJR9ScmL2CXYp-U0KUcE5h9mAEroWMByv4)

### 代码高亮支持
![Code Highlight](https://private-user-images.githubusercontent.com/251222/412806713-aa02cdb1-719f-4973-bf04-4b5ab75a5a34.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk0Mzc1MDMsIm5iZiI6MTczOTQzNzIwMywicGF0aCI6Ii8yNTEyMjIvNDEyODA2NzEzLWFhMDJjZGIxLTcxOWYtNDk3My1iZjA0LTRiNWFiNzVhNWEzNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxM1QwOTAwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YmVmMDI1MTk1OTE3NWQ0OGQ5NjlmMjNlZGRmYzg4YTlhZWFjYmFhNWExMGM3NzI1OTcxMDRhZDkxN2I1MzFmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.NGclgo4z1h0_4GyT7d57iQJB7oR604bRw0gyQfipiqY)

### 数学公式支持
![Formula](https://private-user-images.githubusercontent.com/251222/412806711-58284ce9-13d1-4e02-af9d-f9cf97f96fc8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk0Mzc1MDMsIm5iZiI6MTczOTQzNzIwMywicGF0aCI6Ii8yNTEyMjIvNDEyODA2NzExLTU4Mjg0Y2U5LTEzZDEtNGUwMi1hZjlkLWY5Y2Y5N2Y5NmZjOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxM1QwOTAwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mYWE0YWRjZTI0YzFiODUxZGU3NjcxYjk4YzdkODNkNDlhNDU4ZmVjNWE2ZDM3ZmVjNzY4OTllMzFlZmViNWU2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.s55xib4kLQmbVcjsqUKhx-OE17vgB7CJkTt-wjCWLuU)

### 业务配置

路径：http://localhost:5001/settings

![Settings](https://private-user-images.githubusercontent.com/251222/412811781-44822c8d-ccba-435f-8e54-0fed90263afa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk0MzgxOTIsIm5iZiI6MTczOTQzNzg5MiwicGF0aCI6Ii8yNTEyMjIvNDEyODExNzgxLTQ0ODIyYzhkLWNjYmEtNDM1Zi04ZTU0LTBmZWQ5MDI2M2FmYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxM1QwOTExMzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lODkxYjJkOWE0NzcxY2JiMjVkYjY3ZGY4YzI0ZjliZjNhZDM2NTBlNzIwZjdiMjY3MjE1ZWM3NTIwMjBiMDk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.NFkCO1fqWb1GEhRO_0l0HQazbF2qzjrOV7xQc3bqgXI)

## 主要功能

### 核心功能
- **智能对话服务**
  - 支持多轮次专业对话
  - 实时流式响应
  - 对话历史管理
  - 自动记忆上下文

### 业务配置
- **可定制的提示词系统**
  - 系统提示词配置
  - 用户提示词模板
  - 助手响应规则
  - 欢迎消息定制
  - 最大对话轮次设置

### 系统管理
- **统一身份认证**
  - Basic Auth 管理员认证
  - 可配置的权限体系
- **多模型支持**
  - DeepSeek系列模型集成
  - 可扩展的模型接入框架

  ## 安装步骤
  ```bash
  git clone https://github.com/Zhengquan/chatbot-fullstack-demo.git
  cd chatbot-fullstack-demo
  pip install -r requirements.txt
  python app.py
  ```
  
  ## 配置说明

	```json
	{
	    "models":
	    {
	        "deepseek-r1":
	        {
	            "name": "DeepSeek R1",
	            "api_model": "模型ID",
	            "base_url": "API基础URL",
	            "api_key": "API密钥",
	            "description": "模型描述"
	        }
	    },
	    "admin":
	    {
	        "username": "管理员用户名",
	        "password": "管理员密码"
	    }
	}
	}
	```

## 使用说明

### 访问系统
- 首页：访问 `http://localhost:5001/`
- 设置页面：访问 `http://localhost:5001/settings`（需要管理员认证）

### 管理员认证
- 使用config.json中配置的用户名和密码进行Basic认证
- 所有API接口和管理页面都需要认证
- 静态资源无需认证

## 安全建议

1. 修改默认管理员密码
2. 使用HTTPS保护传输安全
3. 定期更新API密钥
4. 限制服务器访问IP

