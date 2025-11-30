FROM python:3.12-slim-bookworm

RUN useradd -m wagtail

EXPOSE 8080

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=2.1.3 \
    PORT=8080 \
    PATH="/home/wagtail/.local/bin:$PATH"

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

USER wagtail
RUN curl -sSL https://install.python-poetry.org | python - && pip install "gunicorn==20.0.4"
COPY pyproject.toml poetry.lock /
RUN poetry install --no-interaction --no-root --no-ansi

USER root
WORKDIR /app
RUN chown wagtail:wagtail /app
COPY --chown=wagtail:wagtail . .

USER wagtail
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 kmstca.wsgi:application
