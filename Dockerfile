FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

WORKDIR /Game-of-Life

COPY . .

RUN apt-get update && apt-get install -y python3 python3-pip

RUN python3 -m pip install pytest
