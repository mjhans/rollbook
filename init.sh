#!/usr/bin/env bash

sudo pip install virtualenv

virtualenv --python=python3.5 vrollbook
pip install Django
pip install -U mongoengine