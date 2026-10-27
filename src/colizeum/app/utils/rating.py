from sqlalchemy import between, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from colizeum.app.models import Achievement, AwardType, Groups, Participant


def get_group_interval(param: int, group: Groups):
    if group == Groups.MIDDLE:
        return between(param, 5, 8)
    elif group == Groups.HIGHER:
        return between(param, 9, 11)
    else:
        return between(param, 1, 11)


async def get_rating(session: AsyncSession, group: Groups):
    scores = (select(
        Participant.firstname,
        Participant.lastname,
        Participant.grade,
        func.coalesce(func.sum(AwardType.points), 0).label("total_points")
    ).where(get_group_interval(Participant.grade, group))  # pyright: ignore[reportArgumentType]
         .select_from(Participant)
         .join(Achievement, Achievement.participant_id == Participant.id, isouter=True)
         .join(AwardType, Achievement.award_type_id == AwardType.id, isouter=True)
         .group_by(Participant.id)
         .cte("scores"))

    rank_col = func.rank().over(order_by=desc(scores.c.total_points)).label("rank")

    q = select(
        scores.c.firstname,
        scores.c.lastname,
        scores.c.grade,
        scores.c.total_points,
        rank_col
    ).order_by(rank_col, scores.c.lastname, scores.c.firstname)

    res = await session.execute(q)

    return res.fetchall()
