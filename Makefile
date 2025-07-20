REPO_NAME := firedrill
DESCRIPTION := "Run on-call training simulations locally with GPT-4."
PRIVATE := false  # set to true if you want a private repo

.PHONY: all init create push protect start

all: init create push protect

init:
	git init
	git checkout -b main
	echo "# $(REPO_NAME)" > README.md
	git add README.md
	git commit -m "Initial commit"

create:
	gh repo create $(REPO_NAME) \
		--$(if $(filter true,$(PRIVATE)),private,public) \
		--description $(DESCRIPTION) \
		--source=. \
		--remote=origin \
		--push \
		--confirm

push:
	git push -u origin main

setup:
	./setup.sh

start:
	@echo "Running Firedrill simulation..."
	source .venv/bin/activate && python firedrill.py ./scenarios/cache_ttl_misconfig.yaml
