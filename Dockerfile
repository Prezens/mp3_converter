FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /mp3_converter

WORKDIR /mp3_converter

RUN apt-get update && apt-get install -y ffmpeg

COPY . /mp3_converter/

RUN pip install -r requirements.txt

EXPOSE 8000