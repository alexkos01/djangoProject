from django.urls import path

from notes import views

urlpatterns = [
    path('notes/', views.index),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
