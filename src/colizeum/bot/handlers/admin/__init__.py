from aiogram import Router

from . import start

router = Router(name="admin")

router.include_routers(
    start.router,
)
