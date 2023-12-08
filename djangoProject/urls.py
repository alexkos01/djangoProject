
from django.contrib import admin
from django.urls import path, include

from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('author/', views.author),
    path('info/', views.info),
    path('news/', include('news.urls')),
    path('todo/', include('todo.urls')),
    path('todo_reg/', include('todo.urls_reg'))
]
