help:
	@echo "help  -- print this help"
	@echo "start -- start docker stack"
	@echo "stop  -- stop docker stack"
	@echo "ps    -- show status"
	@echo "build  -- build image"
	@echo "clean -- clean all artifacts"
	@echo "test  -- run tests using docker"
	@echo "dockershell -- run bash inside docker"
	@echo "shell_plus -- run django shell_plus inside docker"
	@echo "bootstrap --build containers, run django migrations, load fixtures and create the a superuser"

build:
	docker-compose build filosofes

start:
	docker-compose up -d filosofes

logs:
	docker-compose logs -f --tail=30 filosofes

up:
	docker-compose up filosofes

stop:
	docker-compose stop

ps:
	docker-compose ps

clean: stop
	docker-compose rm --force -v

only_test:
	docker-compose run --rm filosofes pytest

covered_test:
	docker-compose run --rm filosofes pytest addopts=--cov=. --cov-config setup.cfg

pep8:
	docker-compose run --rm filosofes flake8

test: pep8 covered_test

dockershell:
	docker-compose run --rm filosofes /bin/bash

migrations:
	docker-compose run --rm filosofes python manage.py makemigrations --settings=filosofes.settings.docker

migrate:
	docker-compose run --rm filosofes python manage.py migrate --settings=filosofes.settings.docker

superuser:
	docker-compose run --rm filosofes python manage.py createsuperuser --settings=filosofes.settings.docker

shell_plus:
	docker-compose run --rm filosofes python manage.py shell_plus --settings=filosofes.settings.docker

clean-python:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

.PHONY: help start stop ps clean test dockershell shell_plus only_test pep8 clean-python
