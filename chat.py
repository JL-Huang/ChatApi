from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "deepseek-llm"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    
    try:
        res = requests.post(OLLAMA_API_URL, json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False
        })
        res.raise_for_status()
        content = res.json()["message"]["content"]
        return jsonify({"reply": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 
    
