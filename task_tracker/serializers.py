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
    employee = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["title", "deadline"]

    def get_employee(self, instance):
        least_loaded_num_of_tasks = (
            Employee.objects.all().earliest("task__count").task.count()
        )
        return Employee.objects.filter(
            task__count=least_loaded_num_of_tasks
        ) | Employee.objects.filter(task__count=least_loaded_num_of_tasks + 2).filter(
            id=instance.employee.id
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class WorkingEmployeeSerializer(serializers.ModelSerializer):
    number_of_tasks = serializers.SerializerMethodField()
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = "__all__"
        ordering = ["number_of_tasks", "pk"]

    def get_number_of_tasks(self, instance):
        return instance.task.all().filter(status=Task.TaskStatus.IN_PROGRESS).count()

    def get_tasks(self, instance):
        return instance.task.all().filter(status=Task.TaskStatus.IN_PROGRESS)
