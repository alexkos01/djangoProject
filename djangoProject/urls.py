
from django.contrib import admin
from django.urls import path

from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('reg/', views.reg),
    path('authorize/', views.authorize),
    path('user_account/', views.user_account),
]

