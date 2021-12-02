#! /usr/bin/make

ifdef NIX_PROFILE
	USE_NIX:=true
endif

PRIME_LOCUSTFILES=/app/locustfiles/prime.py
OFFICE_LOCUSTFILES=/app/locustfiles/office.py

.PHONY: help
help: ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install_tools
install_tools: ## Install tools needed for project.
	scripts/install_tools

.PHONY: install_python_deps
install_python_deps: ## Install all python dependencies/requirements
	pipenv install

.PHONY: ensure_pre_commit
ensure_pre_commit: .git/hooks/pre-commit ## Ensure pre-commit is installed
.git/hooks/pre-commit: $(shell which pre-commit)
	pre-commit install --install-hooks

.PHONY: pre_commit_update_deps
pre_commit_update_deps: ## Update pre-commit dependencies
	pre-commit autoupdate

.PHONY: pre_commit_tests
pre_commit_tests: ## Run pre-commit tests
	pre-commit run --all-files

.PHONY: setup
setup: install_python_deps ensure_pre_commit ## Installs python dependencies and preps pre-commit

.PHONY: clean
clean: ## Clean all generated files
	find ./ -type d -name '__pycache__' -delete
	find ./ -type f -name '*.pyc' -delete

.PHONY: pretty
pretty: ## Prettify the code
	black .

.PHONY: lint
lint: ## Run linting tests
	flake8 .

.PHONY: generate_readme_toc
generate_readme_toc: ## Re-generates and re-places the table of contents for the README.md
	./gh-md-toc --insert README.md

.PHONY: load_test_prime
load_test_prime: clean ## Run load testing on the Prime API
	open http://localhost:8089
	locust -f locustfiles/prime.py --host local

.PHONY: load_test_office
load_test_office: clean ## Run load testing on the Office app
	open http://localhost:8089
	locust -f locustfiles/office.py --host local

.PHONY: load_test_milmove
load_test_milmove: clean ## Run load testing on the MilMove app
	open http://localhost:8089
	locust -f locustfiles/milmove.py --host local

.PHONY: load_test_prime_workflow
load_test_prime_workflow: clean ## Run load testing on the Prime API
	open http://localhost:8089
	locust -f locustfiles/prime_workflow.py --host local

.PHONY: exp_load_test
exp_load_test: ## Run load testing against the MilMove Experimental Deployment
	export DOCKER_CSV_PREFIX="${DOCKER_CSV_DIR}/$(shell date +'%Y-%m-%d-%H%M%S')"; docker-compose up --build prime-exp-reporting
	docker cp mmlt_prime_exp_reporting:/app/static/reports static/

default: help
