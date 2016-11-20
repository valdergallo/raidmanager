# Make content for developer
help:
	@echo "setup			Instal requirements"
	@echo "test			Run suit test"
	@echo "coverage		Run Coverage"
	@echo "clean			Remove trash files"
	@echo "run			Run Django server"
	@echo "migrate			Run Django migration"
	@echo "postgres			Run Docker Postgresql"
	@echo "postgres_create_db			Create raidmanager database"


run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

setup:
	pip install -r requirements.txt

test:
	# py.test -x
	python manage.py test -v 2 -n --failfast

coverage:
	# rm -rf htmlcov
	# py.test --cov=data_importer --cov-report html
	coverage run manage.py test -v 2 -n
	coverage html -d cover --include=$(shell pwd)/*.*

clean:
	find . -name '*.pyc' -delete
	rm -rf .tox
	rm -rf data_importer.egg-info
	rm -rf cover

postgres:
	docker run --name postgresql -e POSTGRES_PASSWORD=postgres --publish 5432:5432 --volume /opt/postgresql:/var/lib/postgresql -d postgres

postgres_create_db:
	docker exec -it postgresql psql -U postgres -c "CREATE DATABASE \"raidmanager\";"
