
from django.contrib import admin
from django.urls import path, include

from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('author/', views.author),
    path('info/', views.info),
]
