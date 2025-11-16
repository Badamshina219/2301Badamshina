from django.urls import path
from . import views # Импортируем views из текущего приложения

urlpatterns = [
    path('', views.archive, name='archive'), # Корневой путь ('') ведет к представлению archive
]