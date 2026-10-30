import asyncio
from datetime import date

import pytest

from colizeum.app.db import Session
from colizeum.app.utils.users import get_users

expected = [
    (1, 'Ivan', 'Ivanov', 11, date(2026, 10, 27)),
    (2, 'Dima', 'Dmitrov', 9, date(2026, 10, 27)),
    (3, 'Danil', 'Semenov', 6, date(2026, 10, 27)),
    (4, 'Sasha', 'Petrov', 7, date(2026, 10, 27)),
]

@pytest.mark.asyncio()
async def test_get_users():
    async with Session() as session:
        users = await get_users(session)

    assert users == expected
