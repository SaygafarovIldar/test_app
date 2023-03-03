from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100, help_text="Напишите название для категории")
    slug = models.SlugField(verbose_name="Слаг категории", max_length=100,
                            help_text="Переводит название категории, на английские буквы для формирования ссылки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


