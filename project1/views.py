import asyncio

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from project1.bot import main
from project1.models import ModelReg


def edit_img(img):
    user_img = Image.open(img)
    # re_img = user_img.rotate(45)
    # re_img.show()
    # re_img.save(f'media/imgs/{img}')
    user_img.thumbnail(size=(165, 165))
    user_img.show()
    user_img.save(f'media/imgs/{img}')
    return f'media/imgs/{img}'

@csrf_exempt
def main(request):
    if request.method == 'POST':
        asyncio.run(main())
    return render(request, 'main.html')


@csrf_exempt
def reg(request):
    regg = ModelReg()
    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email:
                return render(request, 'main.html', {"err": f'Email: {i.email} занят другим пользователем'})
        regg.email = request.POST['email']
        regg.password = request.POST['password']
        regg.login = request.POST['login']
        regg.img = edit_img(request.FILES['img'])
        regg.save()
        return render(request, 'user_account.html', {'user': f'Пользователь с логином: {regg.login} успешно зарегистрирован!'})
    return render(request, 'reg.html')


@csrf_exempt
def authorize(request):
    regg = ModelReg()
    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email and request.POST['password'] == i.password:
                return render(request, 'user_account.html', {'user': f'Автозизация прошла успешно'})
        return render(request, 'main.html', {'err': 'авторизация не пройдена'})
    return render(request, 'authorize.html')

@csrf_exempt
def user_account(request):
    return render(request, 'user_account.html')


