#!/bin/bash

set -xe

echo "Running migrations"
poetry run python manage.py migrate --noinput

echo "Collecting static files"
poetry run python manage.py collectstatic --noinput

echo "Starting server"
exec "$@"
