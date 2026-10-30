from typing import Any

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback
from colizeum.app.utils.save_achievement import get_award_type_id, is_create_participant, save_achievement
from prettytable import PrettyTable

from colizeum.app.db import Session
from colizeum.app.models import AwardParticipationFormat
from colizeum.app.utils.is_participant import is_participant
from colizeum.bot.filters.is_admin import IsAdmin
from colizeum.bot.keyboards.confirm_kb import (
    ConfirmCallback,
    build_keyboard_for_confirm,
)
from colizeum.bot.keyboards.format_kb import FormatCallback, build_keyboard_for_format
from colizeum.bot.keyboards.grade_kb import GradeCallback, build_keyboard_for_grade
from colizeum.bot.keyboards.level_kb import LevelCallback, build_keyboard_for_level
from colizeum.bot.keyboards.place_kb import PlaceCallback, build_keyboard_for_place


class NewAchievement(StatesGroup):
    fullname = State()
    grade = State()
    format = State()
    level = State()
    place = State()
    event = State()
    received_at = State()
    confirm = State()


router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.message(Command("cancel"))
async def cancel_handler(message: Message, state: FSMContext) -> None:
    await message.answer("Операция отклонена")
    await state.clear()


@router.message(Command("new_achievement"))
async def new_achievement_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("<b>Добро пожаловать в программу добавления достижений!</b>\n\nВведите <i>имя и фамилию</i> ученика (Иван Иванов):\n\nЕсли хотите отменить операцию – введите /cancel на любом шаге")
    await state.set_state(NewAchievement.fullname)


@router.message(F.text, NewAchievement.fullname)
async def capture_fullname(message: Message, state: FSMContext) -> None:
    if message.text is None:
        await message.answer("Операция прервана! Начните заново")
        await state.clear()
        return

    try:
        firstname, lastname = message.text.split(' ')

        await state.update_data(fullname=message.text)

        async with Session() as session:
            flag = await is_participant(session, firstname, lastname)
            if flag:
                await message.answer("Выберите формат достижения:", reply_markup=build_keyboard_for_format())
                await state.set_state(NewAchievement.format)
                return

        await message.answer("Новый ученик! Введите класс обучения участника:", reply_markup=build_keyboard_for_grade())
        await state.set_state(NewAchievement.grade)
    except ValueError:
        await message.answer("Введены некорректные данные! Повторите:")
        return


@router.callback_query(GradeCallback.filter())
async def capture_grade(callback: CallbackQuery, callback_data: GradeCallback, state: FSMContext) -> None:
    await state.update_data(grade=callback_data.grade)
    if isinstance(callback.message, Message):
        await callback.message.edit_text("Выберите формат достижения:", reply_markup=build_keyboard_for_format())
    else:
        await callback.answer("Выберите формат достижения:", reply_markup=build_keyboard_for_format())

    await state.set_state(NewAchievement.format)


@router.callback_query(FormatCallback.filter())
async def capture_format(callback: CallbackQuery, state: FSMContext, callback_data: FormatCallback):
    await callback.answer()

    await state.update_data(format=callback_data.participation_format)

    if callback_data.participation_format == AwardParticipationFormat.CERTIFICATE:
        if isinstance(callback.message, Message):
            await callback.message.edit_text("Введите название мероприятия:")
        else:
            await callback.answer("Введите название мероприятия:")

        await state.set_state(NewAchievement.event)
        return

    if isinstance(callback.message, Message):
        await callback.message.edit_text("Выберите уровень:", reply_markup=build_keyboard_for_level())
    else:
        await callback.answer("Выберите уровень:", reply_markup=build_keyboard_for_level())

    await state.set_state(NewAchievement.level)


@router.callback_query(LevelCallback.filter())
async def capture_level(callback: CallbackQuery, state: FSMContext, callback_data: LevelCallback):
    await callback.answer()

    await state.update_data(level=callback_data.level)

    if isinstance(callback.message, Message):
        await callback.message.edit_text("Выберите место:", reply_markup=build_keyboard_for_place())
    else:
        await callback.answer("Выберите место:", reply_markup=build_keyboard_for_place())

    await state.set_state(NewAchievement.place)


@router.callback_query(PlaceCallback.filter())
async def capture_place(callback: CallbackQuery, state: FSMContext, callback_data: PlaceCallback):
    await callback.answer()

    await state.update_data(place=callback_data.place)

    if isinstance(callback.message, Message):
        await callback.message.edit_text("Введите название мероприятия:")
    else:
        await callback.answer("Введите название мероприятия:")

    await state.set_state(NewAchievement.event)


@router.message(F.text, NewAchievement.event)
async def capture_event(message: Message, state: FSMContext) -> None:
    if message.text is None:
        await message.answer("Операция прервана! Начните заново")
        await state.clear()
        return

    await state.update_data(event=message.text)
    await state.set_state(NewAchievement.received_at)

    await message.answer("Выберите дату проведения:", reply_markup=await SimpleCalendar().start_calendar())


@router.callback_query(SimpleCalendarCallback.filter())
async def capture_date(
    callback: CallbackQuery,
    callback_data: SimpleCalendarCallback,
    state: FSMContext
):
    selected, date = await SimpleCalendar().process_selection(
        callback,
        callback_data
    )

    if selected:
        data = await state.update_data(
            received_at=date.date()
        )

        text = await show_summary(data=data)
        if isinstance(callback.message, Message):
            await callback.message.edit_text(text, reply_markup=build_keyboard_for_confirm())
        else:
            await callback.answer(text, reply_markup=build_keyboard_for_confirm())


        await state.set_state(NewAchievement.confirm)


async def show_summary(data: dict[str, Any], positive: bool = True) -> str:
    fullname = data["fullname"] # strict
    grade = data.get("grade", None)
    format = data["format"] # strict
    level = data.get("level", None)
    place = data.get("place", None)
    event = data["event"] # strict
    received_at = data["received_at"] # strict

    table = PrettyTable()
    table.field_names = ["Поле", "Значение"]
    table.add_divider()

    table.add_row(["ФИ", fullname])
    table.add_divider()

    if grade:
        table.add_row(["Класс", grade])
        table.add_divider()

    table.add_row(["Мероприятие", event])
    table.add_divider()

    table.add_row(["Формат", format.value])
    table.add_divider()

    if format != AwardParticipationFormat.CERTIFICATE and level and place:
        table.add_row(["Уровень", level.value])
        table.add_divider()

        table.add_row(["Место", place.value])
        table.add_divider()

    table.add_row(["Дата", received_at])

    table.align = "l"

    response = f"<pre>{table}</pre>"

    return response


@router.callback_query(ConfirmCallback.filter())
async def capture_confirm(
    callback: CallbackQuery,
    callback_data: ConfirmCallback,
    state: FSMContext
):
    await callback.answer()

    data = await state.update_data(confirm=callback_data.confirm)

    async with Session() as session:
        if data["confirm"]:
            participant_id = await is_create_participant(
                session,
                data["fullname"],
                data.get("grade", None)
            )

            award_type_id = await get_award_type_id(
                session,
                data["format"],
                data["level"],
                data["place"]
            )

            if award_type_id is not None and participant_id is not None:
                await save_achievement(
                    session,
                    participant_id,
                    award_type_id,
                    data["event"],
                    data["received_at"]
                )
            else:
                await callback.answer("Ошибка: достижение не распознано или пользователь не создан/найден", show_alert=True)

            if isinstance(callback.message, Message):
                await callback.message.edit_text("Успешно!")
            else:
                await callback.answer("Успешно!", reply_markup=ReplyKeyboardRemove())
        else:
            if isinstance(callback.message, Message):
                await callback.message.edit_text("Операция отклонена")
            else:
                await callback.answer("Операция отклонена", reply_markup=ReplyKeyboardRemove())
