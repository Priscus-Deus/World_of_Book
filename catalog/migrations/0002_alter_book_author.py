# Generated by Django 5.0 on 2023-12-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Введите название книги', to='catalog.author', verbose_name='Автор книги'),
        ),
    ]