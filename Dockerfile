# syntax=docker/dockerfile:1

FROM python:3.10.11

WORKDIR /imgscroll-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

VOLUME /source_images

ENV IMG_PATH=/source_images

CMD ["python3", "-m", "app"]