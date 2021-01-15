FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

# Copy over and install requirements:
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy over everything else for the app:
COPY docker.__init__.py /app/__init__.py
COPY . /app

EXPOSE 8089 5557

ENTRYPOINT ["locust"]
