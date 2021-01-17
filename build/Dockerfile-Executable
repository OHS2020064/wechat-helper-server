# 基础镜像
FROM bot-server-environment:v1.0.0 AS builder

# 镜像
# 代码添加到镜像
ADD ./ 2020064-wechat-helper-server

# 设置工作目录
WORKDIR 2020064-wechat-helper-server

# 打包
RUN pyinstaller main.spec

# 镜像
RUN cp /opt/2020064-wechat-helper-server/dist/main /opt

WORKDIR /opt

# 基础镜像
FROM ubuntu AS executable

COPY --from=builder /opt/main /opt/2020064-wechat-helper-server/main
COPY --from=builder /opt/2020064-wechat-helper-server/app/core/bot/config.ini /opt/2020064-wechat-helper-server/app/core/bot/config.ini

ENV INF_ENV=True

# 设置工作目录
WORKDIR opt/2020064-wechat-helper-server

ENV PYTHONIOENCODING=utf-8

EXPOSE 80

# 执行
CMD ["./main"]