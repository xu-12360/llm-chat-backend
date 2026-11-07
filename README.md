# 简易LLM对话后端（AI聊天机器人）

> LLM应用开发入门项目：FastAPI 后端 + 智谱GLM大模型 + 网页前端，一个"能聊天、有记忆、会查资料"的完整产品

## ✨ 功能

- **网页聊天界面**：输入问题 → 点发送/按回车 → AI 气泡回复
- **多轮对话记忆**：自动保存整段对话历史，AI 能记住前面聊过的内容（"我叫小明"→"我叫什么"能答出来）
- **知识库问答（RAG）**：提问时先检索本地知识库，命中则带着资料回答，避免编造
- 等待回复时显示"思考中..."提示
- POST /chat 接口：接收用户提问，调用大模型返回回答
- 自动接口文档 /docs 在线调试
- 跨域支持（前端页面可直接调用接口）
- 密钥使用 .env 环境变量管理，不硬编码
- 统一返回格式，异常捕获

## 🛠️ 技术栈

Python 3.11+ | FastAPI | requests | python-dotenv | HTML | JavaScript

## 🧠 技术要点

### 多轮对话记忆
大模型本身没有记忆（无状态），每次请求都是"失忆"的。本项目把整段对话历史（messages 数组）随每次请求一起发给模型，实现连续对话，并控制上下文长度。

### RAG（检索增强生成）

```
用户提问
  → 检索知识库 kb.py（关键词匹配）
  → 命中：把「资料 + 问题」拼进 Prompt，让模型严格照着资料回答
  → 未命中：正常对话，不注入资料
  → 模型返回回答 → 存入对话历史
```

知识库当前用关键词匹配实现（零额外依赖、易理解），可平滑替换为 Embedding 向量检索 + 向量数据库。

## 📂 项目结构

```
llm-chat-backend/
├── main.py           # FastAPI 后端（/chat 接口 + 记忆管理 + RAG 检索）
├── client.py         # 智谱大模型调用（接收 messages 列表）
├── kb.py             # 知识库 + 关键词检索函数
├── index.html        # 前端聊天页面
├── requirements.txt  # 依赖清单
└── .env              # 密钥（已被 .gitignore 忽略，不上传）
```

## 📦 环境部署

```bash
# 创建虚拟环境
python -m venv venv

# windows 激活
venv\Scripts\activate
# mac/linux 激活
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## ⚙️ 配置

新建 .env 文件，填入智谱 API Key（open.bigmodel.cn 免费申请）：

```env
ZHIPU_API_KEY=你的智谱API密钥
```

## 🚀 启动

```bash
# 启动后端
uvicorn main:app --reload
```

然后浏览器直接打开项目里的 `index.html`（双击即可），开始聊天。

接口文档地址：http://127.0.0.1:8000/docs

## 📮 接口示例

POST /chat

```json
{
    "query": "这个项目用了什么技术"
}
```

返回

```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "answer": "..."
    }
}
```

## 📌 迭代路线

- [x] 网页聊天前端
- [x] 多轮对话上下文记忆
- [x] RAG 知识库检索问答
- [x] Agent 工具调用（练手 demo：计算器 / 时钟）
- [ ] Embedding 向量检索替代关键词检索
- [ ] Agent 工具调用接入主项目 /chat 接口
- [ ] 部署上线，支持公网访问
