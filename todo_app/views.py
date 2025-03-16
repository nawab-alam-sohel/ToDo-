from toDo.models import Task
from django. shortcuts import render # type: ignore


def home(request):
    tasks =Task.objects.filter(completed =False).order_by('-update')
    completed_task = Task.objects.filter(completed=True)

    context ={
        'tasks': tasks,
        'completed_task': completed_task,
    }
    return render(request,'home.html ', context) 