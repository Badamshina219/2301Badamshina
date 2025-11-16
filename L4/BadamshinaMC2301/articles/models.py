from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Пользователь как автор
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True) # Дата создания

    def __str__(self): # Используем __str__ вместо __unicode__ для Python 3 / Django > 1.5
        return f"{self.author.username}: {self.title}"

    def get_excerpt(self):
        if len(self.text) > 140:
            return self.text[:140] + "..."
        else:
            return self.text