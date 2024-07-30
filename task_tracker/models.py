from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {"blank": True, "null": True}


class Employee(models.Model):
    last_name = models.CharField(
        max_length=30, verbose_name="Фамилия", help_text="Укажите фамилию сотрудника"
    )
    first_name = models.CharField(
        max_length=30, verbose_name="Имя", help_text="Укажите имя сотрудника"
    )
    middle_name = models.CharField(
        max_length=30,
        **NULLABLE,
        verbose_name="Отчество",
        help_text="Укажите отчество сотрудника",
    )
    position = models.CharField(
        max_length=50,
        verbose_name="Должность",
        help_text="Укажите должность сотрудника",
    )
    info = models.TextField(
        max_length=30,
        **NULLABLE,
        verbose_name="Дополнительная информация",
        help_text="Укажите дополнительную информацию о сотруднике",
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ("pk",)


class Task(models.Model):

    class TaskStatus(models.TextChoices):
        NOT_TAKEN = "Не взятая", _("Не взятая")
        IN_PROGRESS = "Выполняется", _("Выполняется")
        COMPLETED = "Выполненная", _("Выполненная")

    title = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Укажите наименование задачи",
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Родительская задача",
        help_text="Укажите родительскую задачу",
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name="task",
        verbose_name="Исполнитель",
        help_text="Укажите исполнителя задачи",
    )
    deadline = models.DateField(
        verbose_name="Срок", help_text="укажите срок выполнения задачи"
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus,
        default=TaskStatus.NOT_TAKEN,
        verbose_name="Статус",
        help_text="Укажите статус задачи",
    )
    info = models.TextField(
        max_length=30,
        **NULLABLE,
        verbose_name="Дополнительная информация",
        help_text="Укажите дополнительную информацию о задаче",
    )

    def __str__(self):
        return f"{self.title} - {self.status}"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ("pk",)
