# Make content for developer
help:
	@echo "setup			Instal requirements"
	@echo "test			Run suit test"
	@echo "coverage		Run Coverage"
	@echo "clean			Remove trash files"
	@echo "run			Run Django server"
	@echo "migrate			Run Django migration"


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
