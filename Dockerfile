FROM python:3.11


RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-root --with dev --with nox

COPY src/ README.md /app/

RUN POETRY_VIRTUALENVS_CREATE=false poetry install --only-root
