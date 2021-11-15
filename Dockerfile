FROM python:3.9.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# we do not want pipenv to create a virtualenv inside the container
ENV PIPENV_SITE_PACKAGES 1

ARG locustfile
ENV LOCUSTFILE=$locustfile

RUN echo $LOCUSTFILE

WORKDIR /app

RUN pip install pipenv

# Copy over and install Pipfiles and use pip to install requirements
# outside of virtualenv
COPY Pipfile Pipfile.lock /app/
RUN set -x \
    && pipenv lock --keep-outdated --requirements | pip install -r /dev/stdin

# Copy over everything else for the app:
COPY docker.__init__.py /app/__init__.py
COPY locustfiles /app/locustfiles
COPY static /app/static
COPY tasks /app/tasks
COPY utils /app/utils

EXPOSE 8089 5557

ENTRYPOINT ["locust"]
