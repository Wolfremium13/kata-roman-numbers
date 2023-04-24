PIPENV = PIPENV_IGNORE_VIRTUALENVS=1 pipenv
PIPENV_SAFE_RUN = PIPENV_DONT_LOAD_ENV=1 $(PIPENV) run
.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: .venv/lib  ## Install virtualenv dependencies
	@echo "✅ Setup it's done"

.PHONY: tests
tests:  ## Locally run tests
	$(PIPENV) clean
	$(PIPENV_SAFE_RUN) pytest --verbose -s --hypothesis-verbosity=debug

.PHONY: lint
lint:   ## Lint the project files
	@echo "🌑 Formatting with black"
	@$(PIPENV) run black ./src
	@echo "🕵 Check for errors with flake8"
	@$(PIPENV) run flake8 ./
	@echo "😋 Running isort"
	@$(PIPENV) run isort --atomic .

.PHONY: clean
clean: ## Removed venv files
	rm -rf .venv
	$(PIPENV) --rm || true
	$(PIPENV) --rm || true  # two virtualenvs may exists, the local at .venv and the one at ~/.virtualenvs/

.ONESHELL:
.venv/lib: Pipfile.lock
	pip install -U pipenv==v2022.9.24
	$(PIPENV) clean
	mkdir -p .venv
	$(PIPENV) install --dev --no-site-packages
	test -d .venv/lib && touch .venv/lib

.ONESHELL:
Pipfile.lock: Pipfile
	$(PIPENV) lock
