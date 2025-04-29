# chatapi/rag/Dockerfile
FROM python:3.10-slim

# 设置工作目录为 /rag
WORKDIR /rag

# 复制 chatapi/rag 目录下的所有内容到容器中的/rag 目录
COPY . /rag

# 安装 curl 和其他必要工具
RUN apt-get update && apt-get install -y curl

# 安装 Python 依赖包
RUN pip install -r requirements.txt

# 启动 FastAPI 应用
CMD ["uvicorn", "rag:app", "--host", "0.0.0.0", "--port", "8000"]
