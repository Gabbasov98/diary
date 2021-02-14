from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='Имя пользователя',on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя',default='default.png',upload_to='user_images')
    b_data = models.DateField('Дата рождения',default=timezone.now)
    height = models.IntegerField('Рост',default=180)
    weight = models.IntegerField('Вес',default=80)


    def __str__(self):
        return f'Данные пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256,256)
            image.thumbnail(resize)
            image.save(self.img.path)


    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'