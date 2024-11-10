default: fmt fix

project := "project"

# Project management commands
start-app name:
    cd ./{{project}} && uv run manage.py startapp {{name}}

create-superuser:
    cd ./{{project}} && uv run manage.py createsuperuser

# Startup commands
shell:
    cd ./{{project}} && uv run manage.py shell -i ipython

serve:
    cd ./{{project}} && uv run manage.py runserver

# Migrations management commands
make-migrations app="":
    cd ./{{project}} && uv run manage.py makemigrations {{app}}

show-sql app name:
    cd ./{{project}} && uv run manage.py sqlmigrate {{app}} {{name}}

migrate app="":
    cd ./{{project}} && uv run manage.py migrate {{app}}

# Code quality commands
fmt:
    ruff format

lint:
    ruff check

fix:
    ruff check --fix

# Code testing commands
check app="":
    cd ./{{project}} && uv run manage.py check {{app}}

test app="":
    cd ./{{project}} && uv run manage.py test {{app}}

cov app="":
    cd ./{{project}} && coverage run --source="." manage.py test {{app}}

cov-report app="":
    just cov {{app}}
    cd ./{{project}} && coverage report -m

cov-xml app="":
    just cov {{app}}
    cd ./{{project}} && coverage xml -m

cov-html app="":
    just cov {{app}}
    cd ./{{project}} && coverage html -m
