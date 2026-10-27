from aiogram import Router

from . import start

router = Router(name="user")

router.include_routers(
    start.router,
)
