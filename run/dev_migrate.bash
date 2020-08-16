#!/usr/bin/env bash
./manage.py makemigrations --settings=store.settings.development
./manage.py migrate --settings=store.settings.development