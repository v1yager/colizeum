import asyncio

import pytest

from colizeum.app.db import Session
from colizeum.app.models import Groups
from colizeum.app.utils.rating import get_rating

data = [
    {
        "group": Groups.MIDDLE,
        "expected": [
            (4, "Sasha", "Petrov", 7, 25, 1),
            (3, "Danil", "Semenov", 6, 15, 2)
        ],
    },
    {
        "group": Groups.HIGHER,
        "expected": [
            (2, "Dima", "Dmitrov", 9, 35, 1),
            (1, "Ivan", "Ivanov", 11, 20, 2)
        ],
    },
    {
        "group": Groups.TOTAL,
        "expected": [
            (2, "Dima", "Dmitrov", 9, 35, 1),
            (4, "Sasha", "Petrov", 7, 25, 2),
            (1, "Ivan", "Ivanov", 11, 20, 3),
            (3, "Danil", "Semenov", 6, 15, 4)
        ]
    },
]
@pytest.mark.asyncio
@pytest.mark.parametrize("data", data)
async def test_sum_list(data):
    async with Session() as session:
        rating = await get_rating(session, data["group"])

    assert rating == data["expected"]
