#!/bin/bash

cd /home/appuser/app/api

python manage.py migrate

exec "$@"
