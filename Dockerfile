FROM python:3.10.9-slim-buster

WORKDIR /app

RUN useradd appuser && chown appuser ./

RUN pip install --upgrade pip && \
    pip install poetry==1.2.0 && \
    poetry config virtualenvs.create false --local

COPY --chown=appuser poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY --chown=appuser . ./
