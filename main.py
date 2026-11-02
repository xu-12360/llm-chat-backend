from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from client import LLMClient

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


# 请求体模型
class ChatReq(BaseModel):
    query: str


@app.post("/chat")
async def chat(req: ChatReq):
    answer = await llm_client.chat(req.query)
    if answer.startswith("调用失败"):
        return {
            "code": 500,
            "msg": answer,
            "data": None
        }
    return {
        "code": 200,
        "msg": "success",
        "data": {
            "answer": answer
        }
    }


# 启动命令：uvicorn main:app --reload
# 访问文档：http://127.0.0.1:8000/docs
