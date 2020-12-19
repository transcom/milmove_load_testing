FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8089 5557

ENTRYPOINT ["locust"]