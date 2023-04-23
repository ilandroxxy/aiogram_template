"""
В этом файле написаны функции обработчика пользователя
"""

from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

import keyboards.users as kb_users

from utils.enums import inlines, service_info

router = Router()


class CustomCallback(CallbackData, prefix="user"):
    """Пользовательские обратные вызовы"""

    name: str = "Unknown"
    call_data: str = "Unknown"


@router.callback_query(CustomCallback.filter(F.call_data == "main_menu_teacher"))
async def get_menu(call: CallbackQuery) -> None:
    await call.message.edit_text(
        text=f"{service_info.Main.IF_TEACHER.value}",
        reply_markup=kb_users.main.home(),
    )
    await call.answer()


@router.callback_query(CustomCallback.filter(F.call_data == "teacher"))
async def teacher(call: CallbackQuery) -> None:
    await call.message.edit_text(
        text=f"{service_info.Main.IF_TEACHER.value}",
        reply_markup=kb_users.main.teacher_home(),
    )


@router.callback_query(CustomCallback.filter(F.call_data == "student"))
async def student(call: CallbackQuery) -> None:
    await call.message.edit_text(
        text=f"{service_info.Main.IF_STUDENT.value}",
        reply_markup=kb_users.main.student_home(),
    )


# todo: Построить визуальный скелет бота
# todo: Вынести текст из функций обрабатывающих inline кнопки
# todo: Строим приветсвенные сообщения для Студентов и Репетиторов
