import asyncio
from multiprocessing import get_all_start_methods

import pytest

from colizeum.app.db import Session
from colizeum.app.models import AwardLevel, AwardParticipationFormat, AwardPlace
from colizeum.app.utils.save_achievement import get_award_type_id

data = [
    {
        "format": AwardParticipationFormat.PERSONAL,
        "level": AwardLevel.SCHOOL,
        "place": AwardPlace.GRANDPRIX,
        "expected": 1
    },
    {
        "format": AwardParticipationFormat.TEAM,
        "level": AwardLevel.DISTRICT,
        "place": AwardPlace.FIRST,
        "expected": 2
    },
    {
        "format": AwardParticipationFormat.PERSONAL,
        "level": AwardLevel.REGIONAL,
        "place": AwardPlace.SECOND,
        "expected": 3
    },
    {
        "format": AwardParticipationFormat.TEAM,
        "level": AwardLevel.INTERREGIONAL,
        "place": AwardPlace.THIRD,
        "expected": 4
    },
    {
        "format": AwardParticipationFormat.TEAM,
        "level": AwardLevel.INTERREGIONAL,
        "place": AwardPlace.GRANDPRIX,
        "expected": None
    },
]

@pytest.mark.asyncio
@pytest.mark.parametrize("data", data)
async def test_sum_list(data):
    async with Session() as session:
        check = await get_award_type_id(session, data["format"], data["level"], data["place"])

    assert check == data["expected"]
