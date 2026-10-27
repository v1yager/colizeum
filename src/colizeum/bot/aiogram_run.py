import asyncio

from colizeum.bot.create_bot import bot, dp
from colizeum.config import ADMINS


async def main():
    print(ADMINS)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
