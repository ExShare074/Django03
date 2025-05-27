from django.db import models

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_text = models.CharField('Короткое описание новости', max_length=200)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'