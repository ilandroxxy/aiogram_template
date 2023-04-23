from enum import Enum  # StrEnum 3.11+


class Main(Enum):
    CHOICE_ROLE = 'Выберите вашу роль:'
    IF_TEACHER = 'Привет преподаватель, выбери действие:'
    IF_STUDENT = 'Привет студент, выбери действие:'

# todo: Декампозировать классы для Студентов и Репетиторов - сообщения