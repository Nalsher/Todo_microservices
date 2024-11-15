FROM python:latest

COPY . /services

WORKDIR /services


ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

