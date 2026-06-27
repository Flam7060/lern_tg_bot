.DEFAULT_GOAL := help

UV      ?= uv
COMPOSE ?= docker compose
ML_IMAGE ?= oxsecurity/megalinter:v8

.PHONY: help install run lint format fix test ci megalinter ci-full build up down logs clean

help: ## показать список команд
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

## --- разработка ---
install: ## установить зависимости (uv sync --dev)
	$(UV) sync --dev

run: ## запустить бота локально
	$(UV) run python -m app

lint: ## ruff: проверка
	$(UV) run ruff check .

format: ## ruff: отформатировать файлы
	$(UV) run ruff format .

fix: ## ruff: автофиксы + форматирование
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

test: ## запустить тесты
	$(UV) run pytest

## --- ci/cd локально ---
ci: ## то же, что GitHub CI: lint + format-check + tests
	$(UV) run ruff check .
	$(UV) run ruff format --check .
	$(UV) run pytest

megalinter: ## MegaLinter локально (через docker, как в CI)
	docker run --rm -v $(CURDIR):/tmp/lint:rw $(ML_IMAGE)

ci-full: ci megalinter ## полный локальный прогон: ci + megalinter

## --- docker ---
build: ## собрать образ
	$(COMPOSE) build

up: ## поднять бота в docker (фон)
	$(COMPOSE) up -d

down: ## остановить docker
	$(COMPOSE) down

logs: ## смотреть логи docker
	$(COMPOSE) logs -f

## --- прочее ---
clean: ## удалить кеши и отчёты
	rm -rf .ruff_cache .pytest_cache megalinter-reports
	find . -type d -name __pycache__ -exec rm -rf {} +
