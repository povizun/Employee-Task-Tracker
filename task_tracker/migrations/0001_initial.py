# Generated by Django 5.0.7 on 2024-07-28 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Укажите фамилию сотрудника",
                        max_length=30,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Укажите имя сотрудника",
                        max_length=30,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True,
                        help_text="Укажите отчество сотрудника",
                        max_length=30,
                        null=True,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        help_text="Укажите должность сотрудника",
                        max_length=50,
                        verbose_name="Должность",
                    ),
                ),
                (
                    "info",
                    models.TextField(
                        blank=True,
                        help_text="Укажите дополнительную информацию о сотруднике",
                        max_length=30,
                        null=True,
                        verbose_name="Дополнительная информация",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
                "ordering": ("pk",),
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Укажите наименование задачи",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "deadline",
                    models.DateField(
                        help_text="укажите срок выполнения задачи", verbose_name="Срок"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Не взятая", "Не взятая"),
                            ("Выполняется", "Выполняется"),
                            ("Выполненная", "Выполненная"),
                        ],
                        default="Не взятая",
                        help_text="Укажите статус задачи",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "info",
                    models.TextField(
                        blank=True,
                        help_text="Укажите дополнительную информацию о задаче",
                        max_length=30,
                        null=True,
                        verbose_name="Дополнительная информация",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите исполнителя задачи",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="task",
                        to="task_tracker.employee",
                        verbose_name="Исполнитель",
                    ),
                ),
                (
                    "parent_task",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите родительскую задачу",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task_tracker.task",
                        verbose_name="Родительская задача",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
                "ordering": ("pk",),
            },
        ),
    ]
