from fastapi import FastAPI, HTTPException
import requests

# FastAPI应用实例
app = FastAPI()

# DeepSeek API的相关配置
API_KEY = "<DeepSeek API Key>"  # 替换为你的 DeepSeek API Key
BASE_URL = "https://api.deepseek.com"  # Deepseek的API地址

# 请求头
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 路由：用于接收用户消息并返回DeepSeek生成的响应
@app.post("/chat")
async def chat_with_deepseek(user_message: str):
    # 请求体，包含用户消息和系统消息
    data = {
        "model": "deepseek-chat",  # 使用的模型名称
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        "stream": False  # 不进行流式响应，返回完整结果
    }

    try:
        # 向Deepseek API发送POST请求
        response = requests.post(f"{BASE_URL}/v1/chat/completions", headers=headers, json=data)

        # 检查API响应
        if response.status_code == 200:
            response_data = response.json()
            # 返回生成的消息内容
            return {"message": response_data['choices'][0]['message']['content']}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# 服务器启动命令
# uvicorn server_name:app --reload
