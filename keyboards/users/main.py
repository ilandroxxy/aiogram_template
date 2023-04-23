from aiogram.types import InlineKeyboardMarkup

from keyboards.builder import inline_for_user
from utils.enums import inlines


def home(adjust=3) -> InlineKeyboardMarkup:
    """
    Получает кнопки для главного меню пользователя
    :param adjust: Количество кнопок в ряду. По умолчанию 3
    :return:
    """

    keyboards_data = (
        (inlines.BaseCommand.TEACHER.value, "teacher"),
        (inlines.BaseCommand.STUDENT.value, "student"),
        # (inlines.BaseCommand.PARENT.value, "parent"),
    )
    return inline_for_user(keyboards_data, adjust=adjust)


def teacher_home(adjust=2) -> InlineKeyboardMarkup:
    """
    Получает кнопки для главного меню пользователя
    :param adjust: Количество кнопок в ряду. По умолчанию 3
    :return:
    """
    # todo: Поправить документации к функциям, файлам
    keyboards_data = (
        (inlines.Teacher.GET_STUDENTS.value, "get_students"),
        (inlines.Teacher.GET_CONSPECT.value, "get_conspect"),
        (inlines.Teacher.ADD_STUDENT.value, "add_student"),
        (inlines.Teacher.GET_CALENDAR.value, "get_calendar"),
        (inlines.BaseCommand.BACK_TO_MAIN.value, "main_menu_teacher")
    )
    return inline_for_user(keyboards_data, adjust=adjust)

def student_home(adjust=1) -> InlineKeyboardMarkup:
    """
    Получает кнопки для главного меню пользователя
    :param adjust: Количество кнопок в ряду. По умолчанию 3
    :return:
    """
    keyboards_data = (
        (inlines.Student.HAVE_TUTOR.value, "HAVE_TUTOR"),
        (inlines.Student.DONT_HAVE_TUTOR.value, "DONT_HAVE_TUTOR"),
        (inlines.BaseCommand.BACK_TO_MAIN.value, "main_menu_teacher")
    )
    return inline_for_user(keyboards_data, adjust=adjust)


if __name__ == '__main__':
    print(inlines.BaseCommand.TEACHER.value)
    print(inlines.BaseCommand.TEACHER)
