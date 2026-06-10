from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Task, Department
from .forms import TaskForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def task_list(request):
    profile = request.user.profile
    if profile.is_supervisor:
        tasks = Task.objects.all().order_by('department', 'deadline')
        department = "Всі підрозділи"
    else:
        try:
            department = profile.department
            tasks = Task.objects.filter(department=department)
        except:
            tasks = Task.objects.none()
            department = None
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'department': department,
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    if not request.user.profile.is_manager and not request.user.profile.is_supervisor:
        messages.error(request, 'Недостатньо прав.')
        return redirect('task_list')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, 'Завдання створено!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Нове завдання'})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if not request.user.profile.is_manager and not request.user.profile.is_supervisor:
        messages.error(request, 'Недостатньо прав.')
        return redirect('task_list')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Завдання оновлено!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Редагувати завдання'})