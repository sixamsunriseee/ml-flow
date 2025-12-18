FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml .
COPY uv.lock .

RUN uv sync

COPY app/ /app

ENTRYPOINT ["uv", "run", "streamlit", "run", "/app/app.py"]
