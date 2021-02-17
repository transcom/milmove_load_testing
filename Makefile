#! /usr/bin/make

ifndef PY_VERSION
	PY_VERSION = 3.8.3
endif
ifndef VENV_NAME
	VENV_NAME = locust-venv
endif
VENV_DIR = $(HOME)/.pyenv/versions/$(PY_VERSION)/envs/$(VENV_NAME)

ifeq ($(VIRTUAL_ENV),$(VENV_DIR))
	IN_VENV:=true
endif

.PHONY: help
help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv:  ## Setup the local python version and the virtualenv
	pyenv versions | grep -q "$(PY_VERSION)" || pyenv install -v $(PY_VERSION)
	pyenv local $(PY_VERSION)
	pyenv virtualenv $(PY_VERSION) $(VENV_NAME) || echo "Using existing $(VENV_NAME)..."
ifndef IN_VENV
	@echo "Activate your virtualenv using the following commands:\n\n  pyenv activate $(VENV_NAME)\n\n" \
	"Alternatively, set the virtualenv to auto-activate with:\n\n  pyenv local $(VENV_NAME)"
endif

# This target checks that we're in an activated virtualenv for the sake of the following requirements installation:
.PHONY: ensure_venv
ensure_venv:  ## Ensure that the virtualenv is activated
ifeq ($(IN_VENV),true)
	@echo "$(VENV_NAME) has been activated."
else
	@echo "To proceed, activate your virtualenv using the following command:\n\n  pyenv activate $(VENV_NAME)\n"
	false
endif

.PHONY: install
install: ensure_venv requirements.txt requirements-dev.txt  ## Install all requirements
	brew list libev || brew install libev
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# This target ensures that the pre-commit hook is installed and kept up to date if pre-commit updates.
.PHONY: ensure_pre_commit
ensure_pre_commit: .git/hooks/pre-commit  ## Ensure pre-commit is installed
.git/hooks/pre-commit: /usr/local/bin/pre-commit
	pre-commit install
	pre-commit install-hooks

.PHONY: pre_commit_update_deps
pre_commit_update_deps:  ## Update pre-commit dependencies
	pre-commit autoupdate

# Alias/shortcut for pre_commit_update_deps:
.PHONY: update_deps
update_deps: pre_commit_update_deps

.PHONY: pre_commit_tests
pre_commit_tests:  ## Run pre-commit tests
	pre-commit run --all-files

.PHONY: setup
setup: install ensure_pre_commit

.PHONY: clean
clean:  ## Clean all generated files
	find ./ -type d -name '__pycache__' -delete
	find ./ -type f -name '*.pyc' -delete

.PHONY: teardown
teardown:  ## Uninstall the virtualenv and remove all files
	-pyenv uninstall $(VENV_NAME)

.PHONY: pretty
pretty: ensure_venv  ## Prettify the code
	black .

.PHONY: lint
lint: ensure_venv  ## Run linting tests
	flake8 .

.PHONY: load_test_prime
load_test_prime: clean ensure_venv  ## Run load testing on the Prime API
	open http://localhost:8089
	locust -f locustfiles/prime.py --host local

.PHONY: load_test_office
load_test_office: clean ensure_venv  ## Run load testing on the Office app
	open http://localhost:8089
	locust -f locustfiles/office.py --host local

.PHONY: load_test_milmove
load_test_milmove: clean ensure_venv  ## Run load testing on the MilMove app
	open http://localhost:8089
	locust -f locustfiles/milmove.py --host local

.PHONY: load_test_prime_workflow
load_test_prime_workflow: clean ensure_venv  ## Run load testing on the Prime API
	open http://localhost:8089
	locust -f locustfiles/prime_workflow.py --host local

.PHONY: local_docker_build
local_docker_build: clean  ## Build a Docker container to run load testing locally
	docker-compose -f docker-compose.local.yaml build

.PHONY: local_docker_up
local_docker_up: ## Run load testing on the Prime API in local using a Docker container
	open http://localhost:8089
	docker-compose -f docker-compose.local.yaml up

.PHONY: local_docker_down
local_docker_down:  ## Shutdown any active local docker containers with docker-compose
	docker-compose -f docker-compose.local.yaml down

.PHONY: exp_load_test
exp_load_test: ## Run load testing against the MilMove Experimental Deployment
	docker-compose up --build prime-exp-reporting
	docker cp mmlt_prime_exp_reporting:/app/static/reports static/

default: help
