# 基础镜像
FROM python:3.7.0 AS builder

# 添加依赖
ADD ./requirements.txt opt/requirements.txt

# 设置工作目录
WORKDIR opt

# 安装支持
#-i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get -y install vim
