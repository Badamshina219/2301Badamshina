from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Article # Импортируем модель Article из текущего приложения

def archive(request):
    # Получаем все объекты Article из базы данных
    all_articles = Article.objects.all()
    # Передаем их в шаблон 'archive.html' под именем 'posts'
    return render(request, 'archive.html', {"posts": all_articles})