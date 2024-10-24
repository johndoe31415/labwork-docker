FROM ubuntu:24.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install --yes git build-essential pkg-config libcjson-dev openjdk-17-jdk gradle libbcprov-java libgoogle-gson-java libssl-dev gcc g++ libbotan-2-dev nlohmann-json3-dev python3 python3-pip rustc cargo iputils-ping telnet wget && rm -fr /var/cache/apt/* /var/lib/apt/lists/*
RUN pip3 install --break-system-packages cryptography requests

RUN GO_VERSION=$(wget -qO- https://go.dev/VERSION?m=text | head -n 1) && wget https://go.dev/dl/${GO_VERSION}.linux-amd64.tar.gz && rm -rf /usr/local/go && tar -C /usr/local -xzf ${GO_VERSION}.linux-amd64.tar.gz && rm -rf ${GO_VERSION}.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin
