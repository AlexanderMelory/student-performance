# Generated by Django 5.0.1 on 2024-01-04 13:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('peoples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000, verbose_name='Название факультета')),
                ('room', models.PositiveIntegerField(default=1, verbose_name='Номер комнаты')),
                ('housing', models.PositiveIntegerField(default=1, verbose_name='Номер корпуса')),
                ('phone', models.CharField(blank=True, default='Отсутствует', max_length=30, verbose_name='Номер телефона')),
                ('leader', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='peoples.stuff', verbose_name='Декан')),
                ('teachers', models.ManyToManyField(related_name='faculties', to='peoples.stuff', verbose_name='Преподаватели')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000, verbose_name='Название кафедры')),
                ('room', models.PositiveIntegerField(default=1, verbose_name='Номер комнаты')),
                ('housing', models.PositiveIntegerField(default=1, verbose_name='Номер корпуса')),
                ('phone', models.CharField(blank=True, default='Отсутствует', max_length=30, verbose_name='Номер телефона')),
                ('leader', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to='peoples.stuff', verbose_name='Заведующий')),
                ('teachers', models.ManyToManyField(related_name='departments', to='peoples.stuff', verbose_name='Преподаватели')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.faculty', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000, verbose_name='Название группы')),
                ('date_start', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата поступления')),
                ('students', models.ManyToManyField(related_name='student_groups', to='peoples.student', verbose_name='Студенты')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField(default=1, verbose_name='Оценка')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statement', to='peoples.student', verbose_name='Студент')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statement', to='main.studentgroup', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Ведомость',
                'verbose_name_plural': 'Ведомости',
                'ordering': ('-student',),
            },
        ),
    ]
