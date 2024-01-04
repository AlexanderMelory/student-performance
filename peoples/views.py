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

    def get_success_url(self):
        return self.object.get_detail_url()


class StudentUpdateView(UpdateView):
    """
    Редактирование студента
    """

    model = Student
    template_name = 'peoples/students/update.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return self.object.get_detail_url()


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

    def get_success_url(self):
        return self.object.get_detail_url()


class StuffUpdateView(UpdateView):
    """
    Редактирование сотрудника
    """

    model = Stuff
    template_name = 'peoples/stuff/update.html'
    form_class = StuffUpdateForm

    def get_success_url(self):
        return self.object.get_detail_url()


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
