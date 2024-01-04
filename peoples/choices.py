from django.db.models import IntegerChoices


class StuffRole(IntegerChoices):
    """
    Роли Сотрудников
    """

    TEACHER = 1, 'Преподаватель'
    CHIEF = 5, 'Заведующий'
    DEAN = 10, 'Декан'
