FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY docker.__init__.py /app/__init__.py
COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 8089 5557

ENTRYPOINT ["locust"]