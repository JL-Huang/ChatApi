#!/bin/bash

# 构建镜像
docker build -t chat-api .

# 删除已有的容器（如果存在）
docker rm -f chat-api-container 2>/dev/null

# 运行容器（11434 为服务端口，可根据你项目修改）
docker run -d -p 11434:11434 --name chat-api-container chat-api

echo "✅ 服务已启动：访问 http://129.204.24.176:11434"
