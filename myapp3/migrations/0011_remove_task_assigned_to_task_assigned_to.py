# Generated by Django 4.2.dev20221108194129 on 2024-04-13 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp3", "0010_remove_task_assigned_to2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="assigned_to",
        ),
        migrations.AddField(
            model_name="task",
            name="assigned_to",
            field=models.ManyToManyField(
                blank=True, related_name="tasks", to="myapp3.employee"
            ),
        ),
    ]
