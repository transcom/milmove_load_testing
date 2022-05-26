FROM python:3.10.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# we do not want pipenv to create a virtualenv inside the container
ENV PIPENV_SITE_PACKAGES 1

WORKDIR /app

RUN pip install --no-cache-dir pipenv==2022.4.8

# Copy over and install Pipfiles and use pip to install requirements
# outside of virtualenv
COPY Pipfile Pipfile.lock /app/
# Copy in the local openapi_client libraries referenced by Pipfile
COPY openapi_client /app/openapi_client
RUN set -x \
    && pipenv install --system --deploy --site-packages --ignore-pipfile \
    && rm -rf /root/.local/share/virtualenv /root/.local/share/virtualenvs

# Copy over everything else for the app:
COPY docker.__init__.py /app/__init__.py
COPY locustfiles /app/locustfiles
COPY static /app/static
COPY tasks /app/tasks
COPY utils /app/utils
COPY fixtures /app/fixtures

EXPOSE 8089 5557

ENTRYPOINT ["locust"]
