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
	pipenv install --dev

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

.PHONY: test_coverage
test_coverage:
	pipenv run pytest \
	--ignore=openapi_client \
	--junit-xml=junit/report.xml \
	--cov-report html:coverage_html \
	--cov=utils

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

.PHONY: load_test_local
load_test_local:
	locust -f locustfiles/queue.py --host local -u 10

.PHONY: load_test_local_headless
load_test_local_headless:
	locust -f locustfiles/queue.py --host local -u 10 -t 30s --headless

default: help
