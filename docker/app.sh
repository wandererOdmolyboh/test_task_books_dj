#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Filling database with initial data"
python manage.py loaddata library/fixtures/books.json

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
