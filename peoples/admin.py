from django.contrib import admin
from peoples.models import Student, Stuff


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Админка: Student"""

    pass


@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    """Админка: Stuff"""

    pass
