default: fmt fix

# Project management commands
project := "project"

start-app name:
    cd ./{{project}} && uv run manage.py startapp {{name}}

shell:
    cd ./{{project}} && uv run manage.py shell -i ipython

serve:
    cd ./{{project}} && uv run manage.py runserver

# Code quality commands
fmt:
    ruff format

lint:
    ruff check

fix:
    ruff check --fix
