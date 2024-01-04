from django.contrib import admin
from main.models import Statement, Faculty, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Админка: Department"""

    pass


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    """Админка: Faculty"""

    pass


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    """Админка: Statement"""

    pass
