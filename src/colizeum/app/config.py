import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
assert BOT_TOKEN != None, "Переменная BOT_TOKEN не задана в окружении"

DATABASE_URL = os.getenv("DATABASE_URL")
assert DATABASE_URL != None, "Переменная DATABASE_URL не задана в окружении"
