import asyncio
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from project1.models import ModelReg
from project1.bot import mainn
from PIL import Image, ImageDraw
import numpy as np


def edit_img(img):
    orig_img = Image.open(img)
    orig_img.thumbnail(size=(165, 165))
    height, width = orig_img.size
    npImage = np.array(orig_img)
    new_img = Image.new('L', orig_img.size, 0)
    draw = ImageDraw.Draw(new_img)
    draw.pieslice([0, 0, height, width], 0, 360, fill=255)
    np_new = np.array(new_img)
    npImage = np.dstack((npImage, np_new))
    final_img = Image.fromarray(npImage)
    final_img.save(f'media/imgs/{img}', 'png')
    return f'media/imgs/{img}'


@csrf_exempt
def main(request):
    if request.method == 'POST':
        asyncio.run(mainn())
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
        return render(request, 'user_account.html', {'user': f'Пользователь с логином: {regg.login} успешно зарегистрирован!',
                                                     'img': f'{regg.img}'})
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

