from django.shortcuts import render


def news(request):
    return render(request, 'news.html')


def news_day(request):
    return render(request, 'news_day.html')


def news_anons(request):
    return render(request, 'news_anons.html')
