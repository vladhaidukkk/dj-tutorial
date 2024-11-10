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
    uv run ruff format
    uv run djlint ./{{project}} --reformat

check-fmt:
    uv run ruff format --check
    uv run djlint ./{{project}} --check

lint:
    uv run ruff check
    uv run djlint ./{{project}} --lint

fix:
    uv run ruff check --fix

# Code testing commands
check app="":
    cd ./{{project}} && uv run manage.py check {{app}}

test app="":
    cd ./{{project}} && uv run manage.py test {{app}}

cov app="":
    cd ./{{project}} && uv run coverage run --source="." manage.py test {{app}}

cov-report app="":
    just cov {{app}}
    cd ./{{project}} && uv run coverage report -m

cov-xml app="":
    just cov {{app}}
    cd ./{{project}} && uv run coverage xml -m

cov-html app="":
    just cov {{app}}
    cd ./{{project}} && uv run coverage html -m
