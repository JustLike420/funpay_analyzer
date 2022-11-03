from django.db import models


# Create your models here.
class Seller(models.Model):
    username = models.CharField(max_length=100, verbose_name='Ник')
    user_url = models.URLField(verbose_name='Сылка на профиль')
    rating = models.IntegerField(verbose_name='Отзывы')


class Offer(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    type = models.CharField(max_length=100, verbose_name='Тип')
    other = models.CharField(max_length=100, verbose_name='Другое')
    rare = models.CharField(max_length=100, verbose_name='Раритетность')
    quality = models.CharField(max_length=100, verbose_name='Качество')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Продавец')
    href = models.URLField(verbose_name='Сылка на предложение')
    count = models.IntegerField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена')
