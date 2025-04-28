from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 改成 /api/generate
OLLAMA_API_URL = "http://ollama:11434/api/generate"
MODEL_NAME = "deepseek-llm"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    # 提取最后一条用户输入作为 prompt
    prompt = messages[-1]["content"] if messages else ""

    try:
        res = requests.post(OLLAMA_API_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })
        res.raise_for_status()
        content = res.json()["response"]  # 注意！返回字段是 response，不是 message.content
        return jsonify({"reply": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
