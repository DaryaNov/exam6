from django.db import models


STATUS_CHOICES = [
    ('active', 'Активно'),
    ( 'blocked', 'Заблокировано')
]


class Article(models.Model):
    name_author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')


    def __str__(self):
        return "{}. {}".format(self.name_author, self.status)

    class Meta:
        verbose_name_plural = 'Записи'
