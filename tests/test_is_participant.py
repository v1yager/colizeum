import asyncio

import pytest

from colizeum.app.db import Session
from colizeum.app.utils.is_participant import is_participant

data = [
    {
        "firstname": "Dima",
        "lastname": "Dmitrov",
        "expected": True,
    },
    {
        "firstname": "Sasha",
        "lastname": "Petrov",
        "expected": True,
    },
    {
        "firstname": "dima",
        "lastname": "dmItrOv",
        "expected": True,
    },
    {
        "firstname": "Nikita",
        "lastname": "Ivanov",
        "expected": False,
    },
]
@pytest.mark.asyncio
@pytest.mark.parametrize("data", data)
async def test_sum_list(data):
    async with Session() as session:
        check = await is_participant(session, data["firstname"], data["lastname"])

    assert check == data["expected"]
