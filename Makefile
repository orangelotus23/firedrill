REPO_NAME := firedrill
DESCRIPTION := "Run on-call training simulations locally with GPT-4."

.PHONY: setup start start-random list

all: setup start

setup:
	./setup.sh

start:
	@echo "Running Firedrill simulation..."
	source .venv/bin/activate && \
	python ./src/firedrill.py $(if $(SCENARIO),$(SCENARIO),./scenarios/cache_ttl_misconfig.yaml)

start-random:
	@SCENARIO=$$(find ./scenarios -type f -name '*.yaml' | awk 'BEGIN {srand()} {print rand(), $$0}' | sort -n | head -n1 | cut -d' ' -f2-); \
	echo "🔥 Starting random scenario: $$SCENARIO"; \
	make start SCENARIO="$$SCENARIO"

list:
	@echo "Available Firedrill Scenarios:"
	@find ./scenarios -name '*.yaml' -exec basename {} \;

help:
	@echo "Firedrill CLI"
	@echo ""
	@echo "make start SCENARIO=./scenarios/xyz.yaml     # Run a specific scenario"
	@echo "make start-random                            # Run a random scenario"
	@echo "make list                                    # List available scenario files"

.DEFAULT_GOAL := help
