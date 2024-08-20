#!/bin/bash

cd landingpage
pip install -r requirements.txt
python manage.py collectstatic --noinput