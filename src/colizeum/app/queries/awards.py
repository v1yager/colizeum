from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from colizeum.app.models import (
    AwardLevel,
    AwardParticipationFormat,
    AwardPlace,
    AwardType,
)


async def get_award_type_id(
    session: AsyncSession,
    format: AwardParticipationFormat,
    level: AwardLevel | None,
    place: AwardPlace | None
) -> int | None:
    q = select(AwardType.id).where(
        AwardType.format == format,
        AwardType.level == level,
        AwardType.place == place
    )

    award_type_id = await session.scalar(q)

    return award_type_id
