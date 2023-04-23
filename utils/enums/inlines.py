from enum import Enum  # StrEnum 3.11+


class BaseCommand(Enum):
    TEACHER = "Репетитор"
    STUDENT = "Студент"
    PARENT = "Родитель"
    BACK_TO_MAIN = "Главное меню"

class Teacher(Enum):
    """
    Класс с текстами для inline кнопок преподавателя
    """
    GET_STUDENTS = "Список студентов"
    GET_CONSPECT = "Получить конспект"
    ADD_STUDENT = "Добавить студента"
    GET_CALENDAR = 'Заглянуть в расписание'

class Student(Enum):
    """
    Класс с текстами для inline кнопок преподавателя
    """
    HAVE_TUTOR = "Уже есть Преподаватель"
    DONT_HAVE_TUTOR = "Я ищу Преподавателя"

# todo: Класс для инлайн кнопок всех
# todo: Писать подробные комментарие (и к коммитам)
