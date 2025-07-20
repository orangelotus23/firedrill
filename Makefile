REPO_NAME := firedrill
DESCRIPTION := "Run on-call training simulations locally with GPT-4."

.PHONY: setup start

all: setup start

setup:
	./setup.sh

start:
	@echo "Running Firedrill simulation..."
	source .venv/bin/activate && \
	python ./src/firedrill.py $(if $(SCENARIO),$(SCENARIO),./scenarios/cache_ttl_misconfig.yaml)

list:
	@echo "Available Firedrill Scenarios:"
	@find ./scenarios -name '*.yaml' -exec basename {} \;
