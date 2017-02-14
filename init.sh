#!/usr/bin/env bash

sudo pip install virtualenv

virtualenv --python=python3.5 vrollbook
pip install Django

pip install git+https://github.com/django-nonrel/django@nonrel-1.5
pip install git+https://github.com/django-nonrel/djangotoolbox
pip install git+https://github.com/django-nonrel/mongodb-engine