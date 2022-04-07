# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.12-bullseye as base

FROM base as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

FROM python:3.8.12-slim-bullseye

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV LANG C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    tzdata \
    libpq-dev \
    && echo "America/Mazatlan" > /etc/timezone \
    && dpkg-reconfigure tzdata \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && echo 'LANG="en_US.UTF-8"'>/etc/default/locale \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN  groupadd -g 1000 appuser \
    && useradd --no-log-init --shell /bin/bash -u 1000 -g 1000 -o -c "" -m appuser \
    && cp -r /etc/skel/. /home/appuser \
    && chown -R 1000:1000 /home/appuser

USER appuser

COPY --chown=appuser:appuser . /home/appuser/app

WORKDIR /home/appuser/app/api

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]

#CMD gunicorn  --bind 0.0.0.0:$PORT core.wsgi --error-logfile - --access-logfile - --workers 4
CMD gunicorn --bind 0.0.0.0:$PORT core.wsgi
