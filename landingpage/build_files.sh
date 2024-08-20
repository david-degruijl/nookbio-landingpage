#!/bin/bash

# Move into the correct directory
cd landingpage

# Install dependencies
pip install -r ../requirements.txt

# Collect static files
python manage.py collectstatic --noinput