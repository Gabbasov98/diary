from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.urls import reverse


class Day(models.Model):
    date = models.DateField(default=datetime.date.today)
    author = models.ForeignKey(User, verbose_name='Автор', default='', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} '

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def get_absolute_url(self):
        return reverse('plan-main')


class GoalForDays(models.Model):
    date = models.ForeignKey(Day, on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Основной текст')
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'Цель {self.author} на {self.date}; '

    class Meta:
        verbose_name = 'Цель на день'
        verbose_name_plural = 'Цели на день'

