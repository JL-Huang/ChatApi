FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录到容器内
COPY . /app

# 更新 apt-get 并安装 curl 和其他必要工具
RUN apt-get update && apt-get install -y curl

# 安装 Python 依赖包
RUN pip install -r requirements.txt

# 暴露端口 5000
EXPOSE 5000

# 启动 Flask 服务
CMD ["python", "app/chat.py"]
