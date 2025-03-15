from toDo.models import Task
from django. shortcuts import render # type: ignore


def home(request):
    tasks =Task.objects.filter(completed =False).order_by('-update')
    context ={
        'tasks': tasks,
    }
    return render(request,'home.html ', context) 