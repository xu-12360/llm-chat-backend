# 简易LLM对话后端

> LLM应用开发入门项目，FastAPI + Python，对接大模型API提供对话接口

## ✨ 功能

- POST接口对话，接收用户提问，调用大模型返回回答
- 自动接口文档 /docs 在线调试
- 跨域支持，方便后续对接前端
- 密钥使用.env环境变量管理，不硬编码
- 统一返回格式，异常捕获

## 🛠️ 技术栈

Python 3.11+ | FastAPI | requests | python-dotenv

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

新建 .env 文件，填入大模型API KEY：

```env
QWEN_API_KEY=xxx
QWEN_MODEL_NAME=qwen-turbo
QWEN_API_URL=https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation
```

## 🚀 启动

```bash
uvicorn main:app --reload
```

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

1. 增加对话上下文记忆
2. 接入RAG知识库检索
3. 接入Agent工具调用
