from django.views.generic import CreateView, UpdateView, ListView, DetailView

from main.forms import FacultyUpdateForm, FacultyCreateForm, DepartmentUpdateForm, DepartmentCreateForm, \
    StatementUpdateForm, StatementCreateForm
from main.models import Department, Faculty, Statement


class DepartmentCreateView(CreateView):
    """
    Создание Кафедры
    """

    model = Department
    template_name = 'main/departments/create.html'
    form_class = DepartmentCreateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class DepartmentUpdateView(UpdateView):
    """
    Редактирование Кафедры
    """

    model = Department
    template_name = 'main/departments/update.html'
    form_class = DepartmentUpdateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class DepartmentListView(ListView):
    """
    Список Кафедр
    """

    model = Department
    template_name = 'main/departments/list.html'


class DepartmentDetailView(DetailView):
    """
    Просмотр Кафедры
    """

    model = Department
    template_name = 'main/departments/detail.html'


class FacultyCreateView(CreateView):
    """
    Создание Факультета
    """

    model = Faculty
    template_name = 'main/faculties/create.html'
    form_class = FacultyCreateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class FacultyUpdateView(UpdateView):
    """
    Редактирование Факультета
    """

    model = Faculty
    template_name = 'main/faculties/update.html'
    form_class = FacultyUpdateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class FacultyListView(ListView):
    """
    Список Факультетов
    """

    model = Faculty
    template_name = 'main/faculties/list.html'


class FacultyDetailView(DetailView):
    """
    Просмотр Факультета
    """

    model = Faculty
    template_name = 'main/faculties/detail.html'


class StatementCreateView(CreateView):
    """
    Создание Факультета
    """

    model = Statement
    template_name = 'main/statements/create.html'
    form_class = StatementCreateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class StatementUpdateView(UpdateView):
    """
    Редактирование Факультета
    """

    model = Statement
    template_name = 'main/statements/update.html'
    form_class = StatementUpdateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class StatementListView(ListView):
    """
    Список Факультетов
    """

    model = Statement
    template_name = 'main/statements/list.html'


class StatementDetailView(DetailView):
    """
    Просмотр Факультета
    """

    model = Statement
    template_name = 'main/statements/detail.html'
