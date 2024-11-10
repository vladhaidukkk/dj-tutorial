default: fmt fix

# Project management commands
project := "project"

start-app name:
    cd ./{{project}} && uv run manage.py startapp {{name}}

check:
    cd ./{{project}} && uv run manage.py check

shell:
    cd ./{{project}} && uv run manage.py shell -i ipython

serve:
    cd ./{{project}} && uv run manage.py runserver

make-migration app:
    cd ./{{project}} && uv run manage.py makemigrations {{app}}

make-migrations:
    cd ./{{project}} && uv run manage.py makemigrations

show-sql app name:
    cd ./{{project}} && uv run manage.py sqlmigrate {{app}} {{name}}

migrate:
    cd ./{{project}} && uv run manage.py migrate

test app:
    cd ./{{project}} && uv run manage.py test {{app}}

create-superuser:
    cd ./{{project}} && uv run manage.py createsuperuser

# Code quality commands
fmt:
    ruff format

lint:
    ruff check

fix:
    ruff check --fix
