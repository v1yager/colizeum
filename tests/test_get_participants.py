import asyncio
from datetime import date

import pytest

from colizeum.app.db import Session
from colizeum.app.models import Groups
from colizeum.app.queries.participants import get_participants

data = [
    {
        "group": Groups.MIDDLE,
        "expected": [
            (3, 'Danil', 'Semenov', 6, date(2026, 10, 27)),
            (4, 'Sasha', 'Petrov', 7, date(2026, 10, 27)),
        ],
    },
    {
        "group": Groups.HIGHER,
        "expected": [
            (1, 'Ivan', 'Ivanov', 11, date(2026, 10, 27)),
            (2, 'Dima', 'Dmitrov', 9, date(2026, 10, 27)),
        ],
    },
    {
        "group": Groups.TOTAL,
        "expected": [
            (1, 'Ivan', 'Ivanov', 11, date(2026, 10, 27)),
            (2, 'Dima', 'Dmitrov', 9, date(2026, 10, 27)),
            (3, 'Danil', 'Semenov', 6, date(2026, 10, 27)),
            (4, 'Sasha', 'Petrov', 7, date(2026, 10, 27)),
        ]
    },
]

@pytest.mark.asyncio
@pytest.mark.parametrize("data", data)
async def test_get_rating(data):
    async with Session() as session:
        participants = await get_participants(session, data["group"])

    assert participants == data["expected"]
