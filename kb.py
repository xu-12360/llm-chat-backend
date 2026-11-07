# ===== 项目知识库：关于这个项目本身的问答卡 =====
KB = [
    {
        "keywords": ["项目", "做什么", "干什么", "介绍"],
        "answer": "这是一个 LLM 应用开发入门项目：FastAPI 后端 + 智谱 GLM-4-Flash 大模型 + 网页前端，支持多轮对话记忆和知识库问答（RAG）。"
    },
    {
        "keywords": ["技术栈", "技术", "用什么"],
        "answer": "Python 3.11、FastAPI、requests、python-dotenv、HTML、JavaScript。前端通过 fetch 调用后端 /chat 接口。"
    },
    {
        "keywords": ["RAG", "检索增强"],
        "answer": "RAG（检索增强生成）：提问时先从知识库检索相关资料，再把资料和问题一起交给大模型，让它照着资料回答，避免编造。"
    },
    {
        "keywords": ["功能", "能干什么", "会什么"],
        "answer": "1）网页聊天，支持回车发送和思考中提示；2）多轮对话记忆，能记住前面聊过的内容；3）知识库问答，回答项目相关问题。"
    },
    {
        "keywords": ["谁做", "作者", "学习"],
        "answer": "这是 xu-12360 从零学习 LLM 应用开发的练手项目，10 天从 Python 基础学到 FastAPI、网页前端、GitHub 发布、多轮对话、RAG 和 Agent。"
    },
]

def search_kb(question: str):
    """关键词检索：命中任一关键词就返回对应资料，否则返回 None"""
    for item in KB:
        for kw in item["keywords"]:
            if kw.lower() in question.lower():
                return item["answer"]
    return None
