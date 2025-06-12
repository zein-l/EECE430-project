from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name




class Basic_Employee_Information(models.Model):
    Firstname = models.CharField(max_length=100)
    Middlename = models.CharField(max_length=100)
    Familyname = models.CharField(max_length=100)
    Employeeid = models.IntegerField()
    emailaddress = models.EmailField(max_length = 100)
    contact_number = models.BigIntegerField()
    contact_number_length = models.PositiveSmallIntegerField(default=10)
    country_code = models.CharField(max_length=5, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Custom save method to handle phone number pre-processing
        # Example: Assuming `contact_number` is input as an integer without leading zeros
        self.contact_number_length = len(str(self.contact_number))
        super().save(*args, **kwargs)

    def formatted_contact_number(self):
        # Method to return the contact number in a formatted string based on stored length and country code
        contact_str = str(self.contact_number).zfill(self.contact_number_length)
        if self.country_code:
            return f"+{self.country_code} {contact_str}"
        return contact_str
    def __str__(self):
        return f"{self.Firstname} {self.Middlename} {self.Familyname}"

    Position = models.CharField(max_length = 100)
    Department = models.CharField(max_length = 100)

    Residential = models.CharField(max_length = 300, null=True, blank=True)
    Degree = models.CharField(max_length = 100, null=True, blank=True)
    Specialization = models.CharField(max_length = 300, null=True, blank=True)
    Institution = models.CharField(max_length = 100, null=True, blank=True)
    Previous_work = models.CharField(max_length = 200, null=True, blank=True)
    Contract_start_date = models.DateField(default=timezone.now)
    Contract_end_date = models.DateField(default=timezone.now)
    Salary = models.IntegerField(null=True, blank=True)
    Photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    Documents = models.FileField(upload_to='documents/', null=True, blank=True)




class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ManyToManyField(Basic_Employee_Information, related_name='tasks', blank=True)
    progress = models.IntegerField(default=0)  # Progress in percentage
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    def __str__(self):
        return self.title




class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, related_name='assignments', on_delete=models.CASCADE)
    employee = models.ForeignKey(Basic_Employee_Information, on_delete=models.CASCADE)
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage of task completion by the employee.")

    def __str__(self):
        return f"{self.employee.Firstname} - {self.progress_percentage}% - {self.task.title}"



class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    








class Announcement2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    recipients = models.ManyToManyField('Basic_Employee_Information', related_name='announcements')

    def __str__(self):
        return self.title