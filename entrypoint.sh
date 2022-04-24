#!/bin/bash

python manage.py migrate

# Apply site migrations
echo "Apply site migrations"
sed -i "s,newDomain,$DOMAIN," data/data.json
python manage.py loaddata data/data.json

exec "$@"
