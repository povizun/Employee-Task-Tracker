from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from task_tracker.models import Employee, Task
from task_tracker.serializers import (EmployeeSerializer, TaskSerializer,
                                      UrgentTaskSerializer,
                                      WorkingEmployeeSerializer)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UrgentTaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UrgentTaskSerializer
    queryset = Task.objects.filter(
        parent_task__status=Task.TaskStatus.IN_PROGRESS,
        status=Task.TaskStatus.NOT_TAKEN,
    )


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class WorkingEmployeeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WorkingEmployeeSerializer
    queryset = Employee.objects.all()
