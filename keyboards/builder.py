from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.users import handler_inlines


def inline_for_user(data: tuple[tuple[str, str]],
                    adjust=3) -> InlineKeyboardMarkup:
    """
    Создает кнопки с помощью InlineKeyboardBuilder
    :param data: Данные для кнопки, текст и команда коллбэка
    :param adjust: Количество кнопок в ряду. По умолчанию 3
    :return: Объект InlineKeyboardMarkup
    """

    keyboard = InlineKeyboardBuilder()

    # все кнопки добавляем к объекту инлайн-конпок
    for text, call in data:
        keyboard.button(text=text,
                        callback_data=handler_inlines.CustomCallback(
                            name=text,
                            call_data=call
                        ).pack())

    keyboard.adjust(adjust)  # по adjust кнопки в ряд

    return keyboard.as_markup()
