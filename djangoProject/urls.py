from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('reg/', views.reg),
    path('authorize/', views.authorize),
    path('user_account/', views.user_account)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

