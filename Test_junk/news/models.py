from django.db import models
from django.urls import reverse_lazy

class News(models.Model):

    title = models.CharField(max_length=60, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name="Картинка")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey('Category', blank=True, on_delete=models.SET_NULL, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=60, db_index=True, verbose_name="Название категории")

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']
