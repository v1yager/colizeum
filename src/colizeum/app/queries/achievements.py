from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from colizeum.app.models import (
    Achievement,
)


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
