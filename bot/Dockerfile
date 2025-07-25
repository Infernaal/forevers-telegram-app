FROM python:3.10-slim

# Установим зависимости системы
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /dbdc-telegram-mini-bot

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое проекта
COPY . .

# Запуск
CMD ["python", "bot.py"]
