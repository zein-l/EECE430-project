# Generated by Django 4.2.dev20221108194129 on 2024-04-10 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("myapp3", "0006_basic_employee_information"),
    ]

    operations = [
        migrations.AddField(
            model_name="basic_employee_information",
            name="Contract_end_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Contract_start_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Degree",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Documents",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Institution",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Photo",
            field=models.ImageField(blank=True, null=True, upload_to="photos/"),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Previous_work",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Residential",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Salary",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="basic_employee_information",
            name="Specialization",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]