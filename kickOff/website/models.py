from django.urls import reverse

from django.db import models


# Create your models here.
class Players(models.Model):
    fullName = models.CharField(max_length=255, verbose_name="Имя игрока")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Фото")
    about = models.TextField(blank=True, verbose_name="Про игрока")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    club = models.ForeignKey('Club', on_delete=models.PROTECT, null=True, verbose_name="Клуб игрока")

    def __str__(self):
        return self.fullName

    def get_absolute_url(self):
        return reverse('player', kwargs={'player_slug': self.slug})

    class Meta:
        verbose_name = 'Игроки'
        verbose_name_plural = 'Игроки'
        ordering = ['club']


class Club(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Клуб')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('club', kwargs={'club_slug': self.slug})

    class Meta:
        verbose_name = 'Клубы'
        verbose_name_plural = 'Клубы'
        ordering = ['id']