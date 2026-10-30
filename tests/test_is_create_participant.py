import asyncio

import pytest

from colizeum.app.db import Session
from colizeum.app.utils.save_achievement import is_create_participant

data = [
    {
        "fullname": "Dima Dmitrov",
        "grade": None,
        "expected": 2,
    },
    {
        "fullname": "Sasha Petrov",
        "grade": None,
        "expected": 4,
    },
    {
        "fullname": "dima dmItrOv",
        "grade": None,
        "expected": 2,
    },
    {
        "fullname": "Nikita Ivanov",
        "grade": 8,
        "expected": 5,
    },
]

@pytest.mark.asyncio
@pytest.mark.parametrize("data", data)
async def test_sum_list(data):
    async with Session() as session:
        check = await is_create_participant(session, data["fullname"], data["grade"])

    assert check == data["expected"]
