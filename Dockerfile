FROM python:3.9.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG locustfile
ENV LOCUSTFILE=$locustfile

RUN echo $LOCUSTFILE

WORKDIR /app

# Copy over and install requirements:
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy over everything else for the app:
COPY docker.__init__.py /app/__init__.py
COPY locustfiles /app/locustfiles
COPY static /app/static
COPY tasks /app/tasks
COPY utils /app/utils

EXPOSE 8089 5557

ENTRYPOINT ["locust"]
