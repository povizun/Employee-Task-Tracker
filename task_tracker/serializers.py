from django.db.models import Count
from rest_framework import serializers

from task_tracker.models import Employee, Task
from task_tracker.validators import StatusValidator


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            StatusValidator(status="status", employee="employee"),
        ]


class UrgentTaskSerializer(serializers.ModelSerializer):
    employee = serializers.ModelSerializer

    class Meta:
        model = Task
        fields = ["title", "deadline", "employee"]

    def get_employee(self, instance):
        annotated_queryset = Employee.objects.annotate(number_of_tasks=Count("task"))
        least_loaded_num_of_tasks = annotated_queryset.earliest(
            "number_of_tasks"
        ).number_of_tasks
        return annotated_queryset.filter(
            number_of_tasks=least_loaded_num_of_tasks
        ) | annotated_queryset.filter(
            number_of_tasks=least_loaded_num_of_tasks + 2
        ).filter(
            pk=instance.parent_task.employee.pk
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class WorkingEmployeeSerializer(serializers.ModelSerializer):
    number_of_tasks = serializers.SerializerMethodField()
    tasks = serializers.ModelSerializer

    class Meta:
        model = Employee
        fields = "__all__"
        ordering = ["number_of_tasks", "pk"]

    def get_number_of_tasks(self, instance):
        return instance.task.all().filter(status=Task.TaskStatus.IN_PROGRESS).count()

    def get_tasks(self, instance):
        return instance.task.all().filter(status=Task.TaskStatus.IN_PROGRESS)
