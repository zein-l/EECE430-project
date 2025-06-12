from django import forms
from .models import Announcement2, Employee, Task, Basic_Employee_Information, Event, Announcement
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email']

# Assuming we want to keep TaskForm for just adding a task.
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'start_date', 'end_date', 'status']
        widgets = {
            'assigned_to': forms.CheckboxSelectMultiple(),

        }  # or forms.SelectMultiple() depending on your preference
        
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
class Basic_Employee_Information_Form(forms.ModelForm):
    class Meta:
        model = Basic_Employee_Information
        fields = ['Firstname', 'Middlename', 'Familyname', 'Employeeid', 'emailaddress', 'contact_number', 'Position', 'Department', 'Residential', 'Degree', 'Specialization', 'Institution', 'Previous_work', 'Contract_start_date', 'Contract_end_date', 'Salary', 'Photo', 'Documents']




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']


class AnnouncementForm2(forms.ModelForm):
    class Meta:
        model = Announcement2
        fields = ['title', 'content', 'recipients']
        widgets = {
            'recipients': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipients'].queryset = Basic_Employee_Information.objects.all()