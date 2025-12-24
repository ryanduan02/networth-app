SHELL := /bin/bash

DC ?= docker compose

.PHONY: dev down logs test migrate makemigrations fmt lint

dev:
	$(DC) up --build

down:
	$(DC) down -v

logs:
	$(DC) logs -f --tail=200

test:
	$(DC) run --rm api pytest -q

migrate:
	$(DC) run --rm api alembic upgrade head

makemigrations:
	# usage: make makemigrations MSG="create tables"
	$(DC) run --rm api alembic revision --autogenerate -m "$(MSG)"

fmt:
	$(DC) run --rm api ruff format .
	$(DC) run --rm api ruff check . --fix

lint:
	$(DC) run --rm api ruff check .