
from django.urls import path

from news import views

urlpatterns = [
    path('', views.news),
    path('news_day/', views.news_day),
    path('news_anons/', views.news_anons)
]