FROM python:3.9-slim

RUN apt-get update && apt-get install -y make gcc

WORKDIR /service
ENV PYTHONPATH=$WORKDIR:$PYTHONPATH

COPY requirements/base.txt .
RUN pip install -r base.txt
