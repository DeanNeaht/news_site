from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from accounts.models import User


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок новости')
    text = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, verbose_name='Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('detail_news', kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    eng_title = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
