from django.urls import path
from rest_framework.routers import SimpleRouter

from task_tracker.apps import TaskTrackerConfig
from task_tracker.views import (EmployeeViewSet, TaskViewSet,
                                UrgentTaskRetrieveAPIView,
                                WorkingEmployeeRetrieveAPIView)

app_name = TaskTrackerConfig.name

router = SimpleRouter()
router.register("tasks", TaskViewSet, basename="tasks")
router.register("employees", EmployeeViewSet, basename="employees")

urlpatterns = [
    path("tasks/urgent/", UrgentTaskRetrieveAPIView.as_view(), name="urgent_tasks"),
    path(
        "employees/working/",
        WorkingEmployeeRetrieveAPIView.as_view(),
        name="working employees",
    ),
] + router.urls
