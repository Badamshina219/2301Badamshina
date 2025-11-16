from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article # Импортируем нашу модель Article из текущего пакета (.)

class ArticleAdmin(admin.ModelAdmin): # Класс для настройки отображения модели в админке
    list_display = ('title', 'author', 'get_excerpt', 'created_date') # Указываем, какие поля показывать в списке статей

admin.site.register(Article, ArticleAdmin) # Регистрируем модель Article с настройками ArticleAdmin