#!/bin/sh
## This post project generation script only runs if pipenv is on the machine
command -v pipenv >/dev/null 2>&1 || { echo >&2 "pipenv not found.  Aborting startup script."; exit 1; }

# install necessary dependencies
pipenv install

# download the script files from the template repo
pipenv run python src/scripts/download_scripts.py

{% if cookiecutter.include_examples == 'n' %}

rm etl/*.ipynb
rm etl/*.py
rm eda/*.ipynb
rm publish/*.ipynb

{% endif %}
#git init
#git add .
#git commit -m "Initial commit"
