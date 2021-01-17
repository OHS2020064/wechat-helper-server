REPO_PASSWORD=Password
IMG_VERSION:=v1.0.0
IMG:=`cat Image`$(IMG_VERSION)
CONTAINER_NAME:=information-analysis-server
TARGETPORT:=80
INSTANCE_COUNT=1
NUMBERS:= $(shell seq 1 ${INSTANCE_COUNT})
VECTOR:=`pwd`/financial.word
VECTOR_TARGET:=/opt/2020064-information-analysis-server/app/core/train/resource/financial.word
MOUNT_VECTOR:=type=bind,source=$(VECTOR),target=$(VECTOR_TARGET)
MODEL:=`pwd`/sentiment_checkpoint.keras
MODEL_TARGET:=/opt/2020064-information-analysis-server/app/core/train/sentiment_checkpoint.keras
MOUNT_MODEL:=type=bind,source=$(MODEL),target=$(MODEL_TARGET)
LOG:=`pwd`/log
LOG_TARGET:=/opt/log
MOUNT_LOG:=type=bind,source=$(LOG),target=$(LOG_TARGET)
MOUNT:=1

echo:
	docker ps -a --filter name=^/$(CONTAINER_NAME)$

login:
	cat $(REPO_PASSWORD) | docker login --username=ohsaly --password-stdin  registry.cn-shanghai.aliyuncs.com

run:
	@$(foreach number,$(NUMBERS),\
		if [ $(MOUNT) = 0 ]; then \
			docker run -d -m 150M -p 801$(number):$(TARGETPORT) --name=$(CONTAINER_NAME)$(number) $(IMG); \
		else \
			docker run -d -m 2048M -p 801$(number):$(TARGETPORT) --mount $(MOUNT_VECTOR) --mount $(MOUNT_MODEL) --mount $(MOUNT_LOG) --name=$(CONTAINER_NAME)$(number) $(IMG); \
		fi \
	)

stop:
	@$(foreach number,$(shell seq 1 5),\
		docker stop $(CONTAINER_NAME)$(number) ; \
		docker rm $(CONTAINER_NAME)$(number) || echo; \
	)
