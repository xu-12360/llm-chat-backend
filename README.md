# 简易LLM对话后端（AI聊天机器人）

> LLM应用开发入门项目：FastAPI 后端 + 智谱GLM大模型 + 网页前端，一个完整的"打字聊天"产品

## ✨ 功能

- 网页聊天界面：输入问题 → 点发送/按回车 → AI 气泡回复
- 等待回复时显示"思考中..."提示
- POST /chat 接口：接收用户提问，调用大模型返回回答
- 自动接口文档 /docs 在线调试
- 跨域支持（前端页面可直接调用接口）
- 密钥使用 .env 环境变量管理，不硬编码
- 统一返回格式，异常捕获

## 🛠️ 技术栈

Python 3.11+ | FastAPI | requests | python-dotenv | HTML | JavaScript

## 📂 项目结构

```
llm-chat-backend/
├── main.py           # FastAPI 后端（/chat 接口）
├── client.py         # 智谱大模型调用
├── index.html        # 前端聊天页面
├── requirements.txt  # 依赖清单
└── .env              # 密钥（已被 .gitignore 忽略，不上传）
```

## 📦 环境部署

```bash
# 创建虚拟环境
python -m venv venv

# windows激活
venv\Scripts\activate
# mac/linux激活
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
    "query": "介绍一下RAG"
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

## 📌 后续迭代方向

1. 增加对话上下文记忆（多轮对话）
2. 接入RAG知识库检索
3. 接入Agent工具调用
