# Makefile

# 镜像名称
CHAT_IMAGE=huangjingliang/chat-api
RAG_IMAGE=huangjingliang/rag-api

# 版本
VERSION=latest

# 本地开发使用（用 docker-compose.local.yml）
dev:
	docker-compose -f docker-compose.local.yml up --build

# 关闭本地开发环境
down:
	docker-compose -f docker-compose.local.yml down

# 构建本地镜像
build:
	docker build -t $(CHAT_IMAGE):$(VERSION) ./chat
	docker build -t $(RAG_IMAGE):$(VERSION) ./rag

# 推送到远程仓库（Docker Hub）
push:
	docker push $(CHAT_IMAGE):$(VERSION)
	docker push $(RAG_IMAGE):$(VERSION)

# 生产环境部署（用 docker-compose.prod.yml）
deploy:
	docker-compose -f docker-compose.prod.yml pull
	docker-compose -f docker-compose.prod.yml up -d

# 查看本地日志
logs:
	docker-compose -f docker-compose.local.yml logs -f

# 查看生产日志
logs-prod:
	docker-compose -f docker-compose.prod.yml logs -f

# 清理无用镜像
clean:
	docker image prune -f
