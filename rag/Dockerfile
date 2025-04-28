FROM python:3.10-slim

# 设置工作目录
WORKDIR /chat

# 复制当前目录到容器内
COPY . /chat

# 更新 apt-get 并安装 curl 和其他必要工具
RUN apt-get update && apt-get install -y curl

# 安装 Python 依赖包
RUN pip install -r requirements.txt

