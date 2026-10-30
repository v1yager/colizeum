import enum
from datetime import date

from sqlalchemy import (
    CheckConstraint,
    Enum,
    ForeignKey,
    SmallInteger,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Формат проведения
class AwardParticipationFormat(enum.Enum):
    PERSONAL = "Индивидуальный"
    TEAM = "Командный"
    CERTIFICATE = "Сертификат"

# Масштаб достижения
class AwardLevel(enum.Enum):
    RUSSIAN = "Всероссийский"
    INTERREGIONAL = "Межрегиональный"
    REGIONAL = "Региональный"
    DISTRICT = "Областной"
    MUNICIPAL = "Муниципальный"
    SCHOOL = "Школьный"

# Место
class AwardPlace(enum.Enum):
    GRANDPRIX = "Гран-при"
    FIRST = "Первое"
    SECOND ="Второе"
    THIRD = "Третье"

# Группы (по классам)
class Groups(enum.Enum):
    MIDDLE = "5-8" # Средняя школа
    HIGHER = "9-11" # Старшая школа
    TOTAL = "5-11" # Вся школа


class Base(DeclarativeBase):
    pass

# Пользователь (ученик)
class Participant(Base):
    __tablename__ = "participants"
    __table_args__ = (CheckConstraint(
        "grade BETWEEN 1 AND 11"
    ),)

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(30), nullable=False)
    lastname: Mapped[str] = mapped_column(String(30), nullable=False)
    grade: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    registered_at: Mapped[date] = mapped_column(server_default=func.now())

# Тип достижения (перестановка всех перечислений)
class AwardType(Base):
    __tablename__ = "award_types"
    __table_args__ = (UniqueConstraint("level", "format", "place", "points"), CheckConstraint(
        "points >= 0"
    ))

    id: Mapped[int] = mapped_column(primary_key=True)
    format: Mapped[AwardParticipationFormat] = mapped_column(
        Enum(AwardParticipationFormat, native_enum=False, length=30),
        nullable=False
    )
    level: Mapped[AwardLevel | None] = mapped_column(
        Enum(AwardLevel, native_enum=False, length=30),
    )
    place: Mapped[AwardPlace | None] = mapped_column(
        Enum(AwardPlace, native_enum=False, length=30),
    )
    points: Mapped[int] = mapped_column(nullable=False)

# Достижение
class Achievement(Base):
    __tablename__ = "achievements"
    __table_args__ = (UniqueConstraint("participant_id", "award_type_id", "event", "received_at"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    participant_id: Mapped[int] = mapped_column(
        ForeignKey("participants.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    award_type_id: Mapped[int] = mapped_column(
        ForeignKey("award_types.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    event: Mapped[str] = mapped_column(String(100), nullable=False)
    received_at: Mapped[date] = mapped_column(nullable=False)
