# Generated by Django 5.1.6 on 2025-03-04 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employee", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tracker",
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
                ("title", models.CharField(max_length=100, verbose_name="Название")),
                (
                    "time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Срок выполнения"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("inactive", "Не активна"),
                            ("active", "В работе"),
                            ("complete", "Выполнена"),
                        ],
                        default="inactive",
                        max_length=100,
                        null=True,
                        verbose_name="Статус выполнения",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="employee.employee",
                        verbose_name="Исполнитель",
                    ),
                ),
                (
                    "related_tracker",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tracker.tracker",
                        verbose_name="Связанная приятная задача",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Задачи",
            },
        ),
    ]
