from django.urls import path
from rest_framework.routers import SimpleRouter

from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import (EmployeeViewSet, TaskViewSet,
                                UrgentTaskRetrieveAPIView,
                                WorkingEmployeeRetrieveAPIView)

app_name = TaskTrackerConfig.name

router = SimpleRouter()
router.register("task", TaskViewSet, basename="task")
router.register("employee", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("tasks/urgent/", UrgentTaskRetrieveAPIView.as_view(), name="urgent-task-list"),
    path(
        "employees/working/",
        WorkingEmployeeRetrieveAPIView.as_view(),
        name="working-employee-list",
    ),
] + router.urls
