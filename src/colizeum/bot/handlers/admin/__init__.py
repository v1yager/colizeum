from aiogram import Router

from . import get_participants, new_achievements, rating, start

router = Router(name="admin")

router.include_routers(
    start.router,
    new_achievements.router,
    get_participants.router,
    rating.router
)
