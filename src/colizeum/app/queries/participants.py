from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from colizeum.app.models import Groups, Participant
from colizeum.app.queries.rating import get_group_interval


def to_lower(fullname):
    return [fullname[0].lower(), fullname[1].lower()]


# Check is participant without register
async def is_participant(session: AsyncSession, firstname: str, lastname: str) -> bool:
    query = select(
        Participant.firstname,
        Participant.lastname).select_from(Participant)

    res = await session.execute(query)
    participants = res.fetchall()
    participants = [[name.lower() for name in participant] for participant in participants]

    return [firstname.lower(), lastname.lower()] in participants


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


async def get_participants(session: AsyncSession, group: Groups):
    q = select(
        Participant.id,
        Participant.firstname,
        Participant.lastname,
        Participant.grade,
        Participant.registered_at
    ).select_from(Participant).where(get_group_interval(Participant.grade, group))   # pyright: ignore[reportArgumentType]
    participants = await session.execute(q)
    return participants.fetchall()
