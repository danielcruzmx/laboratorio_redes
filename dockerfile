FROM ubuntu:latest
RUN apt-get update && \
    apt-get -y install \
    net-tools \
    iputils-ping \
    curl \
    iproute2 \
    nano \
    wget \
    traceroute \
    hping3 \
    tcpdump \
    nmap \
    tshark  \
    ettercap-text-only \
    arpwatch \
    python-pip \
    python-setuptools
COPY requirements.txt .
RUN  pip install --no-cache-dir -r requirements.txt 
