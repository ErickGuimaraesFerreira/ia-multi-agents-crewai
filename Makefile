# ══════════════════════════════════════════════════════════════════════════════
# Multi-Agents-IA - Makefile
# Comandos úteis para desenvolvimento
# Desenvolvido com AntiGravity IDE
# ══════════════════════════════════════════════════════════════════════════════

.PHONY: help install dev clean lint format test run

# Cores para output
CYAN := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RESET := \033[0m

help: ## Mostra esta ajuda
	@echo ""
	@echo "$(CYAN)Multi-Agents-IA$(RESET) - Comandos Disponíveis"
	@echo "$(YELLOW)Desenvolvido com AntiGravity IDE$(RESET)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(RESET) %s\n", $$1, $$2}'
	@echo ""

install: ## Instala as dependências do projeto
	pip install -r requirements.txt

dev: ## Instala dependências de desenvolvimento
	pip install -e ".[dev]"
	pre-commit install

clean: ## Limpa arquivos temporários
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name ".mypy_cache" -delete
	find . -type d -name "*.egg-info" -delete
	find . -type f -name ".coverage" -delete
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/

lint: ## Executa linting do código
	flake8 .
	mypy .

format: ## Formata o código
	black .
	isort .

test: ## Executa os testes
	pytest --cov=. --cov-report=term-missing

run: ## Executa o projeto
	python main.py

check: format lint ## Formata e executa linting

all: install check test ## Instalação completa com verificações
