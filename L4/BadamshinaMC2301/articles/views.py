from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article

def archive(request):
    # Получаем все статьи из базы данных
    posts = Article.objects.all()
    # Рендерим шаблон archive.html, передав ему список статей
    return render(request, 'articles/archive.html', {"posts": posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article.html', {"post": post})