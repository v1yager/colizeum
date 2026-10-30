from aiogram import Router

from . import new_achievements, start

router = Router(name="admin")

router.include_routers(
    start.router,
    new_achievements.router
)
