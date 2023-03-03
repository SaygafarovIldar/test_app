from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100, help_text="Напишите название для категории")
    slug = models.SlugField(verbose_name="Слаг категории", max_length=100,
                            help_text="Переводит название категории, на английские буквы для формирования ссылки")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_articles', kwargs={"category_slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
