FROM ubuntu:24.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install --yes git build-essential pkg-config libcjson-dev openjdk-17-jdk libbcprov-java libgoogle-gson-java libssl-dev gcc g++ libbotan-2-dev nlohmann-json3-dev python3 python3-pip rustc cargo iputils-ping telnet wget && rm -fr /var/cache/apt/* /var/lib/apt/lists/*
RUN pip3 install --break-system-packages cryptography requests

RUN wget -qO- https://go.dev/VERSION?m=text | head -n 1 | xargs -I {} wget https://go.dev/dl/{}.linux-amd64.tar.gz && rm -rf /usr/local/go && tar -C /usr/local -xzf go1.23.2.linux-amd64.tar.gz && rm -rf go1.23.2.linux-amd64.tar.gz && apt-get purge -y wget
ENV PATH $PATH:/usr/local/go/bin
