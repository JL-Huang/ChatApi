#!/bin/bash

# 设置容器和镜像名称
CONTAINER_NAME="chat-api-container"
IMAGE_NAME="HuangJingliang/chat-api"  # 使用从 Docker Hub 拉取的镜像

# 启动 Ollama 服务（假设 Ollama 已经安装并且可以通过命令启动）
echo "启动 Ollama 服务..."
ollama start &  # 启动 Ollama 服务并在后台运行

# 删除已有的容器（如果存在）
if docker ps -a | grep -q $CONTAINER_NAME; then
  echo "停止并删除已有容器..."
  docker rm -f $CONTAINER_NAME
fi

# 拉取最新的 Docker 镜像
echo "拉取最新的镜像..."
docker pull $IMAGE_NAME

# 运行容器（5000 是 Flask 的默认端口）
echo "启动新的容器..."
docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME

# 输出部署完成消息
echo "✅ 服务已启动：访问 http://129.204.24.176:5000"
