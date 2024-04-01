from django.shortcuts import render, redirect
from .models import Employee, Task
from .forms import EmployeeForm, TaskForm
from django.http import HttpResponseRedirect

def home(request):
    employee_form = EmployeeForm(request.POST or None)
    task_form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if 'employee_submit' in request.POST and employee_form.is_valid():
            employee_form.save()
            return redirect('/success')
        elif 'task_action_submit' in request.POST and task_form.is_valid():
            # Since TaskForm now handles task assignment and progress updates,
            # we no longer need separate forms for these actions.
            task = task_form.save()
            return redirect('/success')

    tasks = Task.objects.select_related('assigned_to').all()

    context = {
        'employee_form': employee_form,
        'task_form': task_form,
        'tasks': tasks,
    }

    return render(request, 'myapp3/home.html', context)

def success(request):
    return render(request, 'myapp3/success.html')
