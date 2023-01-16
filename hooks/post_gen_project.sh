#!/bin/sh
## This post project generation script only runs if poetry is on the machine
command -v poetry >/dev/null 2>&1 || { echo >&2 "poetry not found.  Aborting startup script."exit 1}

# install necessary dependencies
poetry install

poetry run jupyter nbextension enable --py widgetsnbextension

# create .env file
mv env .env

{% if cookiecutter.template == 'base' %}
  curl -o etl/01-etl.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb
{% endif %}

{% if cookiecutter.template == 'csv' %}
  curl -o etl/01-etl.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/etl-read-csv.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb
{% endif %}

{% if cookiecutter.template == 'ssb' %}
  poetry install --with ssb
  curl -o etl/etl_ssb_api.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/etl_ssb_api.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/eda-ssb.ipynb
  poetry add pyjstat
{% endif %}

{% if cookiecutter.template == 'google sheets' %}
  poetry install --with google
  curl -o etl/01-etl.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/etl-gsheet.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb
{% endif %}

{% if cookiecutter.template == 'gis' %}
  poetry install --with gis
  curl -o etl/01-etl.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/etl-gis.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb
{% endif %}

{% if cookiecutter.template == 'screen scraping' %}
  poetry install --with screenscraping
  curl -o etl/01-etl.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/etl-screen-scraping.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb
{% endif %}

{% if cookiecutter.template == 'nvdb' %}
  poetry install --with nvdb
  curl -o etl/01-etl.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/etl-nvdb.ipynb
  curl -o eda/research.ipynb https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/eda-nvdb.ipynb
{% endif %}

{% if cookiecutter.report_creation == true %}
  poetry install --with report
{% endif %}
