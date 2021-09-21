FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y software-properties-common && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y ssh curl && \
    pip3 install boto3 && \
    pip3 install jsondiff && \
    pip3 install awscli && \
    pip3 install ansible && \
    curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get -y update && apt-get install -y packer
    