#! /usr/bin/make

PRE_COMMIT:=/usr/local/bin/pre-commit

ifdef NIX_PROFILE
	USE_NIX:=true
	PRE_COMMIT:=$(NIX_PROFILE)/bin/pre-commit
endif

PRIME_LOCUSTFILES=/app/locustfiles/prime.py
OFFICE_LOCUSTFILES=/app/locustfiles/office.py

.PHONY: help
help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install_tools
install_tools:  ## Install tools needed for project.
	scripts/install_tools

.PHONY: ensure_venv
ensure_venv:  ## Ensure that the virtualenv is activated.
ifndef VIRTUAL_ENV
	@echo "Virtual env not defined. If you are using nix, make sure it's not disabled. If you aren't using nix, run 'make setup'."
	false
endif

.PHONY: install_python_deps
install_python_deps: ensure_venv ## Install all python dependencies/requirements
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: ensure_pre_commit
ensure_pre_commit: .git/hooks/pre-commit  ## Ensure pre-commit is installed
.git/hooks/pre-commit: $(PRE_COMMIT)
	pre-commit install
	pre-commit install-hooks

.PHONY: pre_commit_update_deps
pre_commit_update_deps:  ## Update pre-commit dependencies
	pre-commit autoupdate

.PHONY: pre_commit_tests
pre_commit_tests:  ## Run pre-commit tests
	pre-commit run --all-files

.PHONY: setup
setup: install_python_deps ensure_pre_commit

.PHONY: clean
clean:  ## Clean all generated files
	find ./ -type d -name '__pycache__' -delete
	find ./ -type f -name '*.pyc' -delete

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
	docker-compose -f docker-compose.local.yaml build locust

.PHONY: local_docker_up
local_docker_up: ## Run load testing on the Prime API in local using a Docker container
	open http://localhost:8089
	LOCUSTFILES=$(PRIME_LOCUSTFILES) docker-compose -f docker-compose.local.yaml up locust

.PHONY: local_docker_down
local_docker_down:  ## Shutdown any active local docker containers with docker-compose
	docker-compose -f docker-compose.local.yaml down locust

.PHONY: local_docker_office_up
local_docker_office_up: ## Run load testing on the GHC API in local using a Docker container
	open http://localhost:8089
	LOCUSTFILES=$(OFFICE_LOCUSTFILES) docker-compose -f docker-compose.local.yaml up locust

.PHONY: local_docker_report
local_docker_report:  ## Run load testing automatically against a local server and generate reports
	export DOCKER_CSV_PREFIX="${DOCKER_CSV_DIR}/$(shell date +'%Y-%m-%d-%H%M%S')"; LOCUSTFILES=$(PRIME_LOCUSTFILES) docker-compose -f docker-compose.local.yaml up --build prime-reporting
	docker cp mmlt_prime_reporting:/app/static/reports static/local/

.PHONY: exp_load_test
exp_load_test: ## Run load testing against the MilMove Experimental Deployment
	export DOCKER_CSV_PREFIX="${DOCKER_CSV_DIR}/$(shell date +'%Y-%m-%d-%H%M%S')"; docker-compose up --build prime-exp-reporting
	docker cp mmlt_prime_exp_reporting:/app/static/reports static/

default: help
