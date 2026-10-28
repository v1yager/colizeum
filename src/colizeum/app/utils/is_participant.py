from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from colizeum.app.models import Participant


def to_lower(fullname):
    return [fullname[0].lower(), fullname[1].lower()]


# Check is participant without register
async def is_participant(session: AsyncSession, firstname, lastname: str) -> bool:
    query = select(
        Participant.firstname,
        Participant.lastname).select_from(Participant)

    res = await session.execute(query)
    participants = res.fetchall()
    participants = [[name.lower() for name in participant] for participant in participants]

    return [firstname.lower(), lastname.lower()] in participants
