FROM ubuntu:16.04

RUN apt-get update && apt-get install -y wget git && apt-get clean && rm -rf /var/cache/apt
RUN apt-get -y autoremove && apt-get -y autoclean
RUN rm -rf /var/cache/apt

RUN apt-get install -y python3 python3-pip python3-tk
RUN pip3 install Pillow

WORKDIR /workspace
COPY . /workspace