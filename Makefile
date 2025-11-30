RUN=poetry run
MANAGE=$(RUN) python manage.py

.PHONY: checkmigrations checkpy dev format migrate migrations superuser test

admin:
	@DJANGO_SUPERUSER_PASSWORD=admin $(MANAGE) createsuperuser --username admin --email "admin@localhost" --noinput

check: checkj2 checkmigrations checkpy

checkmigrations:
	@$(MANAGE) makemigrations --check

checkpy:
	@$(RUN) ruff check .
	@$(RUN) ruff format --check .

dev:
	@$(MANAGE) runserver

format:
	@$(RUN) ruff check --select I --fix .
	@$(RUN) ruff format .

migrate:
	@$(MANAGE) migrate

migrations:
	@$(MANAGE) makemigrations

superuser:
	@$(MANAGE) createsuperuser

test:
	@$(RUN) pytest
