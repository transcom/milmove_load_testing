FROM locustio/locust

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

EXPOSE 8089 8080 9443

CMD ["echo", "Hello World"]