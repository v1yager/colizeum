import asyncio
from datetime import date

import pytest

from colizeum.app.db import Session
from colizeum.app.models import Groups
from colizeum.app.queries.achievements import save_achievement
from colizeum.app.queries.rating import get_rating

data = [
    {
        "group": Groups.TOTAL,
        "expected": [
            (1, "Ivan", "Ivanov", 11, 45, 1),
            (2, "Dima", "Dmitrov", 9, 35, 2),
            (4, "Sasha", "Petrov", 7, 25, 3),
            (3, "Danil", "Semenov", 6, 15, 4)
        ]
    },
]
@pytest.mark.asyncio
@pytest.mark.parametrize("data", data)
async def test_save_achievement(data):
    async with Session() as session:
        await save_achievement(
            session,
            1,
            1,
            "None",
            date(2026, 10, 10)
        )
        rating = await get_rating(session, data["group"])

    assert rating == data["expected"]
