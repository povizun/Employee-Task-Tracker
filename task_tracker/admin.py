from django.contrib import admin

from task_tracker.models import Task, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "position")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "employee", "status", "deadline")
