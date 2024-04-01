from django import forms
from .models import Employee, Task

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email']

# Assuming we want to keep TaskForm for just adding a task.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'progress']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Initialize your form here if needed, for example, set initial values or adjust queryset for 'assigned_to'

    def save(self, commit=True):
        # Custom save method to ensure a task is always created with an assigned employee and progress.
        task = super(TaskForm, self).save(commit=False)
        # Assuming 'assigned_to' and 'progress' are handled appropriately within this form.
        if commit:
            task.save()
        return task
