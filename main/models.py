from datetime import date
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property


class Faculty(models.Model):
    """
    Факультет
    """

    name = models.CharField('Название факультета', max_length=5000)
    leader = models.OneToOneField('peoples.Stuff', verbose_name='Декан', null=True, blank=True, on_delete=models.SET_NULL)
    room = models.PositiveIntegerField('Номер комнаты', default=1)
    housing = models.PositiveIntegerField('Номер корпуса', default=1)
    phone = models.CharField('Номер телефона', max_length=30, blank=True, default='Отсутствует')
    teachers = models.ManyToManyField('peoples.Stuff', verbose_name='Преподаватели', related_name='faculties')

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Department(models.Model):
    """
    Кафедра
    """

    name = models.CharField('Название кафедры', max_length=5000)
    leader = models.OneToOneField(
        'peoples.Stuff', verbose_name='Заведующий', related_name='department', null=True, blank=True, on_delete=models.SET_NULL
    )
    faculty = models.ForeignKey(
        'main.Faculty', verbose_name='Факультет', null=True, blank=True, on_delete=models.SET_NULL
    )
    room = models.PositiveIntegerField('Номер комнаты', default=1)
    housing = models.PositiveIntegerField('Номер корпуса', default=1)
    phone = models.CharField('Номер телефона', max_length=30, blank=True, default='Отсутствует')
    teachers = models.ManyToManyField('peoples.Stuff', verbose_name='Преподаватели', related_name='departments')

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class StudentGroup(models.Model):
    """
    Учебная группа
    """

    name = models.CharField('Название группы', max_length=5000)
    date_start = models.DateField('Дата поступления', default=timezone.now, blank=True)
    course = models.PositiveIntegerField('Курс', default=1),
    students = models.ManyToManyField('peoples.Student', verbose_name='Студенты', related_name='student_groups')

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Statement(models.Model):
    """
    Ведомость
    """

    group = models.OneToOneField(
        'main.StudentGroup', verbose_name='Группа', related_name='statement', on_delete=models.CASCADE
    )
    student = models.OneToOneField(
        'peoples.Student', verbose_name='Студент', related_name='statement', on_delete=models.CASCADE
    )
    grade = models.PositiveIntegerField('Оценка', default=1)

    @cached_property
    def name(self):
        return f'Ведомость студента {self.student} группы {self.group}'

    class Meta:
        verbose_name = 'Ведомость'
        verbose_name_plural = 'Ведомости'
        ordering = ('-student',)

    def __str__(self):
        return self.name
