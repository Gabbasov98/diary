from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Biography(models.Model):
    title = models.CharField(verbose_name='Заглавие',max_length=100)
    text = models.TextField(verbose_name='Основной текст')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,verbose_name='Автор',on_delete=models.CASCADE)

    def __str__(self):
        return f'Aвтор: {self.author}; Tема: {self.title} '

    def get_absolute_url(self):
        return reverse('diary-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Биография'
        verbose_name_plural = 'Биографии'