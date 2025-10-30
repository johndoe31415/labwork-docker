FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --yes curl wget zip git build-essential pkg-config libcjson-dev openjdk-21-jdk libbcprov-java libgoogle-gson-java libguava-java libssl-dev gcc g++ libbotan-2-dev nlohmann-json3-dev libgmp-dev python3 python3-pip iputils-ping telnet wget rustup && rm -fr /var/cache/apt/* /var/lib/apt/lists/*
RUN pip3 install --break-system-packages cryptography requests pyasn1

RUN GO_VERSION=$(wget -qO- https://go.dev/VERSION?m=text | head -n 1) && wget https://go.dev/dl/${GO_VERSION}.linux-amd64.tar.gz && rm -rf /usr/local/go && tar -C /usr/local -xzf ${GO_VERSION}.linux-amd64.tar.gz && rm -rf ${GO_VERSION}.linux-amd64.tar.gz
ENV PATH=$PATH:/usr/local/go/bin

# setup rust environment with rustup
RUN rustup default stable

COPY rust /usr/local/rust
RUN cd /usr/local/rust && cargo vendor

# Downloading and installing gradle
RUN curl -L https://services.gradle.org/distributions/gradle-8.10.2-bin.zip -o /tmp/gradle-8.10.2.zip
RUN unzip /tmp/gradle-8.10.2.zip -d /usr/local/ && mv /usr/local/gradle-8.10.2 /usr/local/gradle
ENV PATH=$PATH:/usr/local/gradle/bin

# Installing gradle plugin dependecy by executing a dummy project that includes
# what we need
COPY gradle /tmp/gradle
WORKDIR /tmp/gradle
RUN bash -c "/usr/local/gradle/bin/gradle --no-daemon dependencies"
RUN rm -rf /tmp/gradle && rm -f /tmp/gradle-8.10.2.zip

WORKDIR /
