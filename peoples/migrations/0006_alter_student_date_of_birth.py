# Generated by Django 5.0.1 on 2024-01-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0005_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]