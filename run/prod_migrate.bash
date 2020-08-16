#!/usr/bin/env bash
./manage.py makemigrations --settings=store.settings.production
./manage.py migrate --settings=store.settings.production