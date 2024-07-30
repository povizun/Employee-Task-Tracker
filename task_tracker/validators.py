from rest_framework import serializers

from task_tracker.models import Task


class StatusValidator:
    def __init__(self, status, employee):
        self.status = status
        self.employee = employee

    def __call__(self, value):
        if value.get(self.employee):
            if value.get(self.status) == Task.TaskStatus.NOT_TAKEN:
                raise serializers.ValidationError(
                    "Если указан сотрудник то задача может или выполняться или быть выполненной"
                )
        else:
            if value.get(self.status) in (
                Task.TaskStatus.COMPLETED,
                Task.TaskStatus.IN_PROGRESS,
            ):
                raise serializers.ValidationError(
                    "Если сотрудник не указан то задача может быть только не взятой"
                )
