# Generated by Django 4.2.dev20221108194129 on 2024-04-20 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp3", "0015_alter_task_assigned_to"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskAssignment",
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
                    "progress_percentage",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Percentage of task completion by the employee.",
                        max_digits=5,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp3.basic_employee_information",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignments",
                        to="myapp3.task",
                    ),
                ),
            ],
        ),
    ]
