#!/bin/bash

# Install the required dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput