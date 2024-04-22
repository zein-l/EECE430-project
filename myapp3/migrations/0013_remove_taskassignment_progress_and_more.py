# Generated by Django 4.2.dev20221108194129 on 2024-04-19 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp3", "0012_event"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="taskassignment",
            name="progress",
        ),
        migrations.AddField(
            model_name="taskassignment",
            name="progress_percentage",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="Percentage of task assigned to the employee.",
                max_digits=5,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="taskassignment",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignments",
                to="myapp3.task",
            ),
        ),
    ]
