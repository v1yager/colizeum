import os

from dotenv import load_dotenv

load_dotenv()


try:
    BOT_TOKEN: str = os.environ["BOT_TOKEN"]
except KeyError:
    raise RuntimeError("Переменная BOT_TOKEN не задана в окружении")

try:
    DATABASE_URL: str = os.environ["DATABASE_URL"]
except KeyError:
    raise RuntimeError("Переменная DATABASE_URL не задана в окружении")
