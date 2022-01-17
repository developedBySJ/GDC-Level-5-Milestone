from turtle import title
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task
# Add your Views Here


def add_task(request):
    title = request.GET.get("task")
    Task(title=title).save()
    return HttpResponseRedirect("/tasks")


def complete_task(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/tasks")


def delete_task(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")


def task_view(request):
    tasks = Task.objects.filter(completed=False, deleted=False)
    return render(request, "task.html", {"path": "pending_tasks", "tasks": tasks})


def home_view(request):
    tasks = Task.objects.filter(deleted=False)
    return render(request, "task.html", {"path": "all_tasks", "tasks": tasks})


def completed_task_view(request):
    tasks = Task.objects.filter(completed=True, deleted=False)
    return render(request, "task.html", {"path": "completed_tasks", "tasks": tasks})
