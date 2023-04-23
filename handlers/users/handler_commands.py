from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import keyboards.users as kb_users
from utils.enums import service_info

router = Router()


@router.message(Command("start"))
async def command_start(msg: Message, state: FSMContext):
    await msg.answer(
        f"Привет, {msg.from_user.first_name}!"
        f" {service_info.Main.CHOICE_ROLE.value}",
        reply_markup=kb_users.home(),
        disable_web_page_preview=True,
    )


@router.message(Command("getmyid"))
async def command_getmyid(msg: Message, state: FSMContext):
    await msg.answer(
        f"Привет, пользователь {msg.from_user.first_name}!\n"
        f"Получи твой ID: {msg.from_user.id}"
    )
