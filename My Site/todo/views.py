from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo


# Create your views here.

def list_todos(request):
    todo_list = Todo.objects.all()  
    # for list in todo_list:
    #     print(list)
    return render(request, 'todolist.html',{'todo_list':todo_list})

def create_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        image = request.FILES.get('image')      
        Todo.objects.create(task=task, image=image)
        return redirect('list_todos')
    return render(request, 'create_todo.html')

def update_todo(request,todo_id):
    # todo_id = request.POST['todo_id']
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.task = request.POST['task']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('list_todos')
    return render(request, 'update_todo.html', {'todo': todo})


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')





