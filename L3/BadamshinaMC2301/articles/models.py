from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Импортируем встроенную модель User

class Article(models.Model):
    title = models.CharField(max_length=200) # Поле для заголовка, строка до 200 символов
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Связь с пользователем (автором). CASCADE означает, что если пользователь удалится, удалятся и его статьи.
    text = models.TextField() # Поле для текста статьи, может быть длинным
    created_date = models.DateField(auto_now_add=True) # Поле для даты создания. auto_now_add=True автоматически устанавливает дату при создании объекта.

    def __unicode__(self): # Метод для строкового представления объекта (для Python 2.x, но может использоваться и в 3.x для обратной совместимости)
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self): # Метод для получения краткого описания (первые 140 символов)
        return self.text[:140] + "..." if len(self.text) > 140 else self.text