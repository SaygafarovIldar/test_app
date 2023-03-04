# Generated by Django 4.1.7 on 2023-03-04 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название поста')),
                ('content', models.TextField(verbose_name='Описание поста')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фотка поста')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления поста')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Категория поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-created_at'],
            },
        ),
    ]
