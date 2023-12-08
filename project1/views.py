import asyncio

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from project1.bot import main
from project1.models import ModelReg


@csrf_exempt
def index(request):
    if request.method == 'POST':
        asyncio.run(main())
    return render(request, 'index.html')


@csrf_exempt
def login(request):
    reg = ModelReg()
    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email:
                return render(request, 'index.html', {"err": f'Email: {i.email} занят другим пользователем'})
        reg.email = request.POST['email']
        reg.password = request.POST['password']
        reg.login = request.POST['login']
        reg.img = request.POST['img']
        reg.save()
        return render(request, 'info.html', {'user': f'Пользователь с логином: {reg.login} успешно зарегистрирован!'})
    return render(request, 'login.html')


@csrf_exempt
def author(request):
    reg = ModelReg()
    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email and request.POST['password'] == i.password:
                return render(request, 'info.html', {'user': f'Автозизация прошла успешно'})
        return render(request, 'index.html', {'err': 'авторизация не пройдена'})
    return render(request, 'author.html')

@csrf_exempt
def info(request):
    return render(request, 'info.html')


