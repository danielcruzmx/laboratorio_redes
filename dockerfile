FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    net-tools \
    iputils-ping \
    curl \
    iproute2 \
    nano \
    traceroute \
    hping3 \
    tcpdump \
    nmap \
    python-pip \
    tshark  \
    ettercap-text-only \
    arpwatch \
    python-setuptools
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
