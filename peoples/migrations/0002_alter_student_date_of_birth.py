# Generated by Django 5.0.1 on 2024-01-04 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(1994, 1, 11, 10, 36, 12, 782887, tzinfo=datetime.timezone.utc), verbose_name='Дата рождения'),
        ),
    ]