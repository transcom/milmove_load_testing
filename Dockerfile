FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . /app

# Certs for mTLS authentication
COPY config/tls/devlocal-mtls.cer /config/tls/devlocal-mtls.cer
COPY config/tls/devlocal-mtls.key /config/tls/devlocal-mtls.key

RUN pip install -r /app/requirements.txt

EXPOSE 8089 5557

ENTRYPOINT ["locust"]
