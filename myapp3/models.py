from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, related_name='tasks', on_delete=models.SET_NULL, null=True, blank=True)
    progress = models.IntegerField(default=0)  # Progress in percentage

    def __str__(self):
        return self.title
