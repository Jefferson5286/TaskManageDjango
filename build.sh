#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "install requeriments"
# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

echo "Start script.py"
python script.py

echo "Migrate"
#  Database migrate
python manage.py makemigrations
python manage.py migrate

echo "collect static"
# Convert static asset files
python manage.py collectstatic --no-input

