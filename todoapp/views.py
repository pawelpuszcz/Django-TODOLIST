from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect

def todoappView(request):
    all_todo_items = Item.objects.all()
    return render(request, 'todolist.html', {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = Item(content =  x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = Item.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
