FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

# Настройки uv
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

# Инструменты для сборки нативных Python-зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости без dev-группы
RUN uv sync --locked --no-dev

# Используем виртуальное окружение проекта
ENV PATH="/app/.venv/bin:$PATH"

# Запускаем бота
CMD ["python", "-m", "colizeum.bot.aiogram_run"]
