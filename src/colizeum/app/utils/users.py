from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from colizeum.app.models import Groups
from colizeum.app.utils.rating import get_group_interval
from colizeum.app.utils.save_achievement import Participant


async def get_users(session: AsyncSession, group: Groups):
    q = select(
        Participant.id,
        Participant.firstname,
        Participant.lastname,
        Participant.grade,
        Participant.registered_at
    ).select_from(Participant).where(get_group_interval(Participant.grade, group))   # pyright: ignore[reportArgumentType]
    participants = await session.execute(q)
    return participants.fetchall()
