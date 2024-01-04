from django import forms
from peoples.models import Student, Stuff


class StudentBaseForm(forms.ModelForm):
    """
    Базовая форма Студента
    """

    class Meta:
        model = Student
        fields = '__all__'


class StudentCreateForm(StudentBaseForm):
    """
    Форма Создание студента
    """

    pass


class StudentUpdateForm(StudentBaseForm):
    """
    Форма Редактирование студента
    """

    pass


class StuffBaseForm(forms.ModelForm):
    """
    Базовая форма сотрудника
    """

    class Meta:
        model = Stuff
        fields = '__all__'


class StuffCreateForm(StuffBaseForm):
    """
    Форма Создание сотрудника
    """

    pass


class StuffUpdateForm(StuffBaseForm):
    """
    Форма Редактирование сотрудника
    """

    pass
