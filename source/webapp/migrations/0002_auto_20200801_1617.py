# Generated by Django 2.2 on 2020-08-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(default='EmailAdress', max_length=100, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name_author',
            field=models.CharField(default='Name', max_length=100, verbose_name='Имя автора'),
        ),
    ]
