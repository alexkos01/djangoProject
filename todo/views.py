from django.shortcuts import render

def todo(request):
    return render(request, 'todo.html')

def todo_reg(request):
    return render(request, 'todo_reg.html')

