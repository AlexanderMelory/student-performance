from datetime import date, timedelta
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from peoples.choices import StuffRole


class Student(models.Model):
    """
    Студент
    """

    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256)
    date_of_birth = models.DateTimeField('Дата рождения', blank=True, null=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('-first_name',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_detail_url(self):
        return reverse_lazy('peoples:student-detail', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse_lazy('peoples:student-edit', kwargs={'pk': self.pk})


class Stuff(models.Model):
    """
    Сотрудник
    """

    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256)
    role = models.IntegerField('Роль', choices=StuffRole.choices, default=StuffRole.TEACHER)
    date_of_birth = models.DateField('Дата рождения', default=date.today() - timedelta(days=30 * 365))

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('-first_name',)

    def __str__(self):
        return f'{self.get_role_display()} {self.first_name} {self.last_name}'

    def get_detail_url(self):
        return reverse_lazy('peoples:stuff-detail', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse_lazy('peoples:stuff-edit', kwargs={'pk': self.pk})
