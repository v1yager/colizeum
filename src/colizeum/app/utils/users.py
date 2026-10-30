from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from colizeum.app.utils.save_achievement import Participant


async def get_users(session: AsyncSession):
    q = select(
        Participant.id,
        Participant.firstname,
        Participant.lastname,
        Participant.grade,
        Participant.registered_at
    ).select_from(Participant)
    participants = await session.execute(q)
    return participants.fetchall()
