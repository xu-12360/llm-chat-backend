import os
import json
import asyncio
import requests
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("ZHIPU_API_KEY")
        self.model = "glm-4-flash"
        self.api_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
        self.timeout = 30

    async def chat(self, prompt: str) -> str:
        """异步调用大模型，返回回答文本"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
              "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                }


        # requests是同步，用线程包装成异步
        try:
            resp = await asyncio.to_thread(
                requests.post,
                self.api_url,
                headers=headers,
                data=json.dumps(payload),
                timeout=self.timeout
            )
            resp.raise_for_status()
            res_json = resp.json()
            return res_json["choices"][0]["message"]["content"]
        except Exception as e:
            return f"调用失败：{str(e)}"


# 本地测试
if __name__ == "__main__":
    c = LLMClient()
    ans = asyncio.run(c.chat("你好"))
    print(ans)
