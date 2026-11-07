from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from client import LLMClient
from kb import search_kb

app = FastAPI(title="简易LLM对话后端")

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_client = LLMClient()
chat_history = []   # 聊天记忆: 存所有轮次

# 请求体模型
class ChatReq(BaseModel):
    query: str


@app.post("/chat")
async def chat(req: ChatReq):
    # 1. 把问题记进记忆本
    chat_history.append({"role": "user", "content": req.query})
    # 2. 先查知识库
    context = search_kb(req.query)
    messages = chat_history.copy()          # 复制一份准备发送
    if context:
        # 查到资料：把最后一条换成"资料 + 问题"的指令
        messages[-1] = {"role": "user", "content": f"""请严格根据下面的资料回答用户问题，资料里没有的信息不要编造。

【资料】{context}

【用户问题】{req.query}"""}
    # 3. 发给模型（带记忆 + 带资料）
    answer = await llm_client.chat(messages)
    # 4. 把 AI 回答记进记忆本
    chat_history.append({"role": "assistant", "content": answer})
    if answer.startswith("调用失败"):
        return {"code": 500, "msg": answer, "data": None}
    return {"code": 200, "msg": "success", "data": {"answer": answer}}



# 启动命令：uvicorn main:app --reload
# 访问文档：http://127.0.0.1:8000/docs
