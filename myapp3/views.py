from audioop import reverse
from django.urls import reverse
import calendar
from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee, Task, Basic_Employee_Information, TaskAssignment , Announcement
from .forms import AnnouncementForm2, EmployeeForm, EventForm, TaskForm, Basic_Employee_Information_Form, AnnouncementForm
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory, modelformset_factory
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseBadRequest
from .models import Event
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.http import Http404
from .utils import Calendar
from datetime import datetime, date
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

def landing_page(request):
    return render(request, 'myapp3/landing.html')

def home(request):
    task_form = TaskForm(request.POST or None)
    if request.method == 'POST' and task_form.is_valid():
        task = task_form.save()
        return redirect('/success')

    tasks = Task.objects.prefetch_related('assigned_to').all()
    context = {
        'task_form': task_form,
        'tasks': tasks,
    }

    return render(request, 'myapp3/home.html', context)



def Manager1(request):
    if request.method == 'POST':
        manager1_form = Basic_Employee_Information_Form(request.POST)
        if manager1_form.is_valid():
            manager1_form.save()
            return redirect('home')
    else:
        manager1_form = Basic_Employee_Information_Form()
    context = {
        'manager1_form': manager1_form
    }
    return render(request, 'myapp3/Manager1.html', context)



def success(request):
    return render(request, 'myapp3/success.html')


def manage_tasks(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.save()
            task_form.save_m2m()  # This is required for saving ManyToMany relations
            return redirect('home')
    else:
        task_form = TaskForm()
    return render(request, 'myapp3/manage_tasks.html', {'task_form': task_form})





def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'myapp3/view_tasks.html', {'tasks': tasks})

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    all_employees = Basic_Employee_Information.objects.all()
    task_assignments = TaskAssignment.objects.filter(task=task).select_related('employee')

    if request.method == 'POST':
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.start_date = request.POST.get('start_date', task.start_date)
        task.end_date = request.POST.get('end_date', task.end_date)
        task.status = request.POST.get('status', task.status)
        task.save()

        # Update or create new assignments for the task
        for employee in all_employees:
            employee_id = str(employee.id)
            if employee_id in request.POST.getlist('assigned_employees'):
                progress = request.POST.get(f'progress_{employee_id}', 0)
                TaskAssignment.objects.update_or_create(
                    task=task,
                    employee=employee,
                    defaults={'progress_percentage': progress}
                )

        messages.success(request, 'Task updated successfully.')
        return redirect('update_tasks')  # Assuming 'update_tasks' is the URL name for the list of tasks

    return render(request, 'myapp3/update_task.html', {
        'task': task,
        'all_employees': all_employees,
        'task_assignments': task_assignments
    })

def update_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'myapp3/update_tasks.html', {'tasks': tasks})


def Manager3(request):
    return render(request, 'myapp3/Manager3.html')


@csrf_exempt
def fetch_events(request):
    # Fetch all events from the database
    events = Event.objects.all()
    event_list = [{
        'id': event.id,
        'title': event.title,
        'start': event.start_time.isoformat(),
        'end': event.end_time.isoformat(),
    } for event in events]
    return JsonResponse(event_list, safe=False)

@csrf_exempt
def add_event(request):
    # Add a new event
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event = Event(
                title=data['title'],
                start_time=datetime.fromisoformat(data['start']),
                end_time=datetime.fromisoformat(data['end'])
            )
            event.save()
            return JsonResponse({'status': 'success', 'event_id': event.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def update_event(request, event_id):
    # Update an existing event
    if request.method == 'POST':
        try:
            event = Event.objects.get(pk=event_id)
            data = json.loads(request.body)
            event.title = data['title']
            event.start_time = datetime.fromisoformat(data['start'])
            event.end_time = datetime.fromisoformat(data['end'])
            event.save()
            return JsonResponse({'status': 'success'})
        except Event.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Event not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def delete_event(request, event_id):
    # Delete an event
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
        return JsonResponse({'status': 'success'})
    except Event.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Event not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


def delete_employee(request):
    employees = Basic_Employee_Information.objects.all()  # Get all employees to display
    return render(request, 'myapp3/delete_employee.html', {'employees': employees})

def perform_delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Basic_Employee_Information, pk=employee_id)
        employee.delete()
        return redirect('delete_employee')  # Redirect to the same page to refresh the list
    return redirect('delete_employee')  # Redirect here if not a POST request


def update_employee(request, employee_id):
    employee = get_object_or_404(Basic_Employee_Information, pk=employee_id)
    if request.method == 'POST':
        form = Basic_Employee_Information_Form(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or any other appropriate page
    else:
        form = Basic_Employee_Information_Form(instance=employee)

    return render(request, 'myapp3/update_employee.html', {'form': form})


def list_employee(request):
    employees = Basic_Employee_Information.objects.all()
    return render(request, 'myapp3/list_employee.html', {'employees': employees})

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'myapp3/list_tasks.html', {'tasks': tasks})

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return redirect('delete_task')
    else:
        return redirect('delete_task')




def assign_tasks(request):
    tasks = Task.objects.all()
    employees = Basic_Employee_Information.objects.all()
    return render(request, 'myapp3/assign_tasks.html', {'tasks': tasks, 'employees': employees})

def assign_employee(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    employees = Basic_Employee_Information.objects.all()
    if request.method == 'POST':
        employee_ids = request.POST.getlist('employees')
        if employee_ids:
            task.assigned_to.clear()  # Clear existing assignments if you want to replace them
            for employee_id in employee_ids:
                employee = Basic_Employee_Information.objects.get(id=employee_id)
                progress_key = f'Task Percentage{employee_id}'
                progress_value = request.POST.get(progress_key, 0)
                # Create or update TaskAssignment
                TaskAssignment.objects.update_or_create(
                    task=task,
                    employee=employee,
                    defaults={'progress_percentage': progress_value}
                )
                task.assigned_to.add(employee)  # This line is optional if TaskAssignment fully replaces the need for M2M
            task.save()
            messages.success(request, 'Employees have been successfully assigned.')
            return redirect('assign_tasks')
        else:
            return redirect('assign_employee', task_id=task_id)
    else:
        return render(request, 'myapp3/assign_employee.html', {'task': task, 'employees': employees})
    

def delete_task(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, f'Task "{task.title}" has been successfully deleted.')
        return redirect('delete_task')
    return render(request, 'myapp3/delete_task.html', {'tasks': tasks})


def post_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    return render(request, 'myapp3/post_announcement.html', {'form': form})

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'myapp3/announcement_list.html', {'announcements': announcements})


def home2(request):
    email = request.GET.get('email')
    employee_id = request.GET.get('employeeId')

    try:
        employee = Basic_Employee_Information.objects.get(emailaddress=email, Employeeid=employee_id)
    except Basic_Employee_Information.DoesNotExist:
        raise Http404("Employee not found or wrong credentials.")

    # Render a different template or pass different context based on employee's role
    # For simplicity, we are rendering the same template with the employee's information
    return render(request, 'myapp3/home2.html', {'employee': employee})

def view_employee(request, employee_id):
    employee = get_object_or_404(Basic_Employee_Information, id=employee_id)
    return render(request, 'myapp3/view_employee.html', {'employee': employee})





def index(request):
    return HttpResponse('Hello from cal!')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'myapp3/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()



def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})




def select_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a confirmation page or back to home
    else:
        form = AnnouncementForm2()

    return render(request, 'myapp3/select_announcement.html', {'form': form})

def page(request):
    return render(request, 'myapp3/page.html')






def see_announcements(request):
    employee_id = request.GET.get('employeeId')
    try:
        if employee_id:
            employee_id = int(employee_id)
            announcements = Announcement.objects.filter(recipients__id=employee_id)
            return render(request, 'myapp3/see_announcements.html', {'announcements': announcements})
        else:
            # Handle the case where no employeeId is provided or it is empty
            return HttpResponse('Employee ID is required.', status=400)
    except ValueError:
        # Handle the case where the employeeId is not a number
        return HttpResponse('Invalid Employee ID.', status=400)