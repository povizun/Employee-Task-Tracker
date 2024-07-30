import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from task_tracker.models import Employee, Task
from users.models import User


# Create your tests here.
class TaskTestCase(APITestCase):
    """Тестирование задач"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@service.py")
        self.user.set_password("123qwe456")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(
            id=4, first_name="Test", last_name="Testov", position="Tester"
        )
        self.task = Task.objects.create(
            title="Buy",
            deadline=datetime.date(2028, 1, 1),
            employee=self.employee,
            status=Task.TaskStatus.IN_PROGRESS,
        )
        self.task_child_task = Task.objects.create(
            title="Buy for buy",
            deadline=datetime.date(2028, 1, 1),
            parent_task=self.task,
        )

    def test_task_create(self):
        """Тест создания задачи"""
        url = reverse("tasks:task-list")
        data = {"title": "Buy", "deadline": datetime.date(2028, 1, 1)}
        response = self.client.post(url, data=data)
        print("\ntest_task_create")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 3)

    def test_task_retrieve(self):
        """Тест получения задачи"""
        url = reverse("tasks:task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url)
        print("\ntest_task_retrieve")
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.task.title)

    def test_task_update(self):
        """Тестирование изменения задачи"""
        url = reverse("tasks:task-detail", kwargs={"pk": self.task.id})
        new_data = {
            "info": "послушать любимую песню",
        }
        response = self.client.patch(url, data=new_data)
        print("\ntest_task_update")
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("info"), "послушать любимую песню")

    def test_task_delete(self):
        """Тестирование удаления задачи"""
        url = reverse("tasks:task-detail", kwargs={"pk": self.task.id})
        response = self.client.delete(url)
        print("\ntest_task_delete")
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.all().count(), 0)

    def test_task_list(self):
        """Тестирование вывода списка задач"""
        url = reverse("tasks:task-list")
        response = self.client.get(url)
        print("\ntest_task_list")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.all().count(), 2)

    def test_urgent_task_list(self):
        """Тестирование вывода списка срочных задач"""
        url = reverse("tasks:urgent-task-list")
        response = self.client.get(url)
        print("\ntest_task_list")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(
                parent_task__status=Task.TaskStatus.IN_PROGRESS,
                status=Task.TaskStatus.NOT_TAKEN,
            ).count(),
            1,
        )

    def test_StatusValidator(self):
        """Тестирование валидации статуса задачи"""
        url = reverse("tasks:task-list")
        data = {
            "title": "Buy",
            "deadline": datetime.date(2028, 1, 1),
            "status": Task.TaskStatus.IN_PROGRESS,
        }
        response = self.client.post(url, data=data)
        print("\ntest_StatusValidator")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class EmployeeTestCase(APITestCase):
    """Тестирование сотрудника"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@service.py")
        self.user.set_password("123qwe456")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(
            id=4, first_name="Test", last_name="Testov", position="Tester"
        )
        self.task = Task.objects.create(
            title="Buy",
            deadline=datetime.date(2028, 1, 1),
            employee=self.employee,
            status=Task.TaskStatus.IN_PROGRESS,
        )

    def test_employee_create(self):
        """Тест создания сотрудника"""
        url = reverse("tasks:employee-list")
        data = {"first_name": "Prog", "last_name": "Progov", "position": "Proger"}
        response = self.client.post(url, data=data)
        print("\ntest_employee_create")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.all().count(), 2)

    def test_employee_retrieve(self):
        """Тест получения сотрудника"""
        url = reverse("tasks:employee-detail", kwargs={"pk": self.employee.id})
        response = self.client.get(url)
        print("\ntest_employee_retrieve")
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("first_name"), self.employee.first_name)

    def test_employee_update(self):
        """Тестирование изменения сотрудника"""
        url = reverse("tasks:employee-detail", kwargs={"pk": self.employee.id})
        new_data = {
            "info": "послушать любимую песню",
        }
        response = self.client.patch(url, data=new_data)
        print("\ntest_employee_update")
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("info"), "послушать любимую песню")

    def test_employee_delete(self):
        """Тестирование удаления сотрудника"""
        url = reverse("tasks:employee-detail", kwargs={"pk": self.employee.id})
        response = self.client.delete(url)
        print("\ntest_employee_delete")
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.all().count(), 0)

    def test_employee_list(self):
        """Тестирование вывода списка сотрудников"""
        url = reverse("tasks:employee-list")
        response = self.client.get(url)
        print("\ntest_employee_list")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.all().count(), 1)

    def test_working_employee_list(self):
        """Тестирование вывода списка занятых сотрудников"""
        url = reverse("tasks:working-employee-list")
        response = self.client.get(url)
        print("\ntest_working_employee_list")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.all().count(), 1)
