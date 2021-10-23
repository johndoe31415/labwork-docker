FROM ubuntu:21.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install --yes git build-essential libcjson-dev openjdk-17-jdk libbcprov-java libssl-dev gcc g++ python3 python3-pip && rm -fr /var/cache/apt/* /var/lib/apt/lists/*
RUN pip3 install cryptography requests
