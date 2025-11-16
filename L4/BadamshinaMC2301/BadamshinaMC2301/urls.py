from django.contrib import admin
from django.urls import path, include # Добавляем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')), # Включаем URL-ы из приложения articles
    # Теперь все URL, начинающиеся с корня (''), будут обрабатываться articles.urls
]