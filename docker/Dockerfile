FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y ssh && \
    pip3 install boto3 && \
    pip3 install jsondiff && \
    pip3 install awscli && \
    pip3 install ansible