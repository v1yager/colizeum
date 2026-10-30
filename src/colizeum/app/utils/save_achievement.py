from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from colizeum.app.models import (
    Achievement,
    AwardLevel,
    AwardParticipationFormat,
    AwardPlace,
    AwardType,
    Participant,
)


async def is_create_participant(
    session: AsyncSession,
    fullname: str,
    grade: int | None
) -> int | None:
    firstname, lastname = [name.lower().capitalize() for name in fullname.split(" ")]
    if grade is None:
        participant_id = await session.scalar(
            select(Participant.id).where(
                Participant.firstname == firstname,
                Participant.lastname == lastname,
            )
        )
    else:
        p = Participant()
        p.firstname = firstname
        p.lastname = lastname
        p.grade = grade

        session.add(p)
        await session.flush()

        participant_id = p.id

    return participant_id


async def get_award_type_id(
    session: AsyncSession,
    format: AwardParticipationFormat,
    level: AwardLevel,
    place: AwardPlace
) -> int | None:
    q = select(AwardType.id).where(
        AwardType.format == format,
        AwardType.level == level,
        AwardType.place == place
    )

    award_type_id = await session.scalar(q)

    return award_type_id


async def save_achievement(
    session: AsyncSession,
    participant_id: int,
    award_type_id: int,
    event: str,
    received_at: date
):
    a = Achievement()
    a.award_type_id = award_type_id
    a.participant_id = participant_id
    a.event = event
    a.received_at = received_at

    session.add(a)
    await session.commit()
