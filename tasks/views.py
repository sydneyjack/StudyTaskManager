
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    """Display all study tasks on the home page."""
    tasks = Task.objects.order_by("completed", "due_date", "-created_at")

    context = {
        "tasks": tasks,
        "total_tasks": Task.objects.count(),
        "completed_tasks": Task.objects.filter(completed=True).count(),
        "pending_tasks": Task.objects.filter(completed=False).count(),
    }

    return render(request, "tasks/home.html", context)


def add_task(request):
    """Save a new study task when the form is submitted."""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        due_date = request.POST.get("due_date") or None

        if title:
            Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
            )
            return redirect("home")

        return render(
            request,
            "tasks/add_task.html",
            {"error": "Please enter a task title."},
        )

    return render(request, "tasks/add_task.html")

def task_detail(request, task_id):
    """Display the details of one study task."""
    task = get_object_or_404(Task, id=task_id)

    return render(request, "tasks/task_detail.html", {"task": task})


def toggle_task(request, task_id):
    """Change a task between completed and pending."""
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()

    return redirect("task_detail", task_id=task_id)

def delete_task(request, task_id):
    """Delete a study task after a delete form is submitted."""
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.delete()

    return redirect("home")
