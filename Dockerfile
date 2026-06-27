# Образ с предустановленным uv и Python 3.13
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Не писать .pyc, логи сразу в stdout (важно для docker logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Непривилегированный пользователь: контейнер не должен работать от root
RUN useradd --create-home --uid 1000 appuser && chown appuser:appuser /app
USER appuser

# 1) Сначала только манифесты — слой с зависимостями кешируется,
#    пока pyproject.toml / uv.lock не меняются
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# 2) Затем код приложения
COPY app ./app

# Запуск точки входа пакета. BOT_TOKEN приходит из окружения контейнера.
CMD ["uv", "run", "--no-dev", "python", "-m", "app"]
