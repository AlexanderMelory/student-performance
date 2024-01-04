from django import forms
from main.models import Department, Faculty, Statement


class DepartmentBaseForm(forms.ModelForm):
    """
    Базовая форма Кафедры
    """

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentCreateForm(DepartmentBaseForm):
    """
    Форма Создание кафедры
    """

    pass


class DepartmentUpdateForm(DepartmentBaseForm):
    """
    Форма Редактирование кафедры
    """

    pass


class FacultyBaseForm(forms.ModelForm):
    """
    Базовая форма Факультета
    """

    class Meta:
        model = Faculty
        fields = '__all__'


class FacultyCreateForm(FacultyBaseForm):
    """
    Форма Создание Факультета
    """

    pass


class FacultyUpdateForm(FacultyBaseForm):
    """
    Форма Редактирование Факультета
    """

    pass


class StatementBaseForm(forms.ModelForm):
    """
    Базовая форма Ведомости
    """

    class Meta:
        model = Statement
        fields = '__all__'


class StatementCreateForm(StatementBaseForm):
    """
    Форма Создание Ведомости
    """

    pass


class StatementUpdateForm(StatementBaseForm):
    """
    Форма Редактирование Ведомости
    """

    pass
