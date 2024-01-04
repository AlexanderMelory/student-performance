from django.views.generic import CreateView, UpdateView, ListView, DetailView
from peoples.forms import StudentCreateForm, StudentUpdateForm, StuffCreateForm, StuffUpdateForm
from peoples.models import Student, Stuff


class StudentCreateView(CreateView):
    """
    Создание студента
    """

    model = Student
    template_name = 'peoples/students/create.html'
    form_class = StudentCreateForm


class StudentUpdateView(UpdateView):
    """
    Редактирование студента
    """

    model = Student
    template_name = 'peoples/students/update.html'
    form_class = StudentUpdateForm


class StudentListView(ListView):
    """
    Список студентов
    """

    model = Student
    template_name = 'peoples/students/list.html'


class StudentDetailView(DetailView):
    """
    Просмотр студента
    """

    model = Student
    template_name = 'peoples/students/detail.html'


class StuffCreateView(CreateView):
    """
    Создание сотрудника
    """

    model = Stuff
    template_name = 'peoples/stuff/create.html'
    form_class = StuffCreateForm


class StuffUpdateView(UpdateView):
    """
    Редактирование сотрудника
    """

    model = Stuff
    template_name = 'peoples/stuff/update.html'
    form_class = StuffUpdateForm


class StuffListView(ListView):
    """
    Список сотрудников
    """

    model = Stuff
    template_name = 'peoples/stuff/list.html'


class StuffDetailView(DetailView):
    """
    Просмотр сотрудника
    """

    model = Stuff
    template_name = 'peoples/stuff/detail.html'
