#################################################################################
# SELF DOCUMENTING HELP                                                                       #
#################################################################################

.DEFAULT_GOAL := help
.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: lab docs build site deploy toc template new nvdb eda etl publish githook

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.project_name }}
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################

##@ Project Management

lab: ## Run Jupyter lab
	poetry run jupyter lab

docs: ## serve the contents of docs
	poetry run mkdocs serve

build: ## build the contents of docs
	make toc
	poetry run mkdocs build

site: ## build the contents of docs and test that it works before deploying
	make build
	cd report_build; \
  	python -m SimpleHTTPServer 1234

deploy: ## deploy the built docs to server
	make build

toc: ## Create a TOC for the docs folder.
	poetry run python src/scripts/populate_mkdocs.py

template: ## Use a template from bord4-templates
	poetry run python src/scripts/download_templates.py

etl: ## Create new file in etl from generic-header
	@read -p "Enter file name for the new template:" filename; \
	curl -o etl/$$filename.ipynb;  https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb \
	echo "Created etl/$$filename.ipynb"

eda: ## Create new file in eda from generic-header
	@read -p "Enter file name for the new template:" filename; \
	curl -o eda/$$filename.ipynb;  https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb \
	echo "Created eda/$$filename.ipynb"

publish:
	@read -p "Enter file name for the new template:" filename; \
	curl -o publish/$$filename.ipynb;  https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb \
	echo "Created pubish/$$filename.ipynb"

githook:
	curl -o .git/hooks/pre-commit;  https://raw.githubusercontent.com/BergensTidende/bord4-analysis-templates/master/templates/generic-header.ipynb

##@ Install Formatting and Linting
.PHONY: lint-Install
lint-Install: ## Install all formatters and linters
	poetry install --with lint

##@ Formatting
.PHONY: format-black
format-black: ## black (code formatter)
	@poetry run black .

.PHONY: format-isort
format-isort: ## isort (import formatter)
	@poetry run isort .

.PHONY: format
format: format-black format-isort ## run all formatters

##@ Linting
.PHONY: lint-black
lint-black: ## black in linting mode
	@poetry run black . --check

.PHONY: lint-isort
lint-isort: ## isort in linting mode
	@poetry run isort . --check

.PHONY: lint-flake8
lint-flake8: ## flake8 (linter)
	@poetry run flake8 .

.PHONY: lint-mypy
lint-mypy: ## mypy (static-type checker)
	@poetry run mypy --config-file pyproject.toml .

.PHONY: lint-mypy-report
lint-mypy-report: ## run mypy & create report
	@poetry run mypy --config-file pyproject.toml . --html-report ./mypy_html

lint: lint-black lint-isort lint-flake8 lint-mypy ## run all linters
