import requests

def chat_with_model(messages):
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "deepseek-llm",
        "messages": messages,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]

if __name__ == "__main__":
    messages = []
    print("开始对话吧！输入 'exit' 退出。\n")

    while True:
        user_input = input("你：")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})
        reply = chat_with_model(messages)
        messages.append({"role": "assistant", "content": reply})
        print("🤖：", reply)