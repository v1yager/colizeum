from aiogram import Router

from . import rating, start

router = Router(name="user")

router.include_routers(
    start.router,
    rating.router
)
