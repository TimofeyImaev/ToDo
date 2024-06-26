from django.http import HttpResponseRedirect
from django.shortcuts import render

from todoapp.models import TodoListItem


# Create your views here.

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'all_items' : all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    TodoListItem.objects.get(id = i).delete()
    return HttpResponseRedirect('/todoapp/')