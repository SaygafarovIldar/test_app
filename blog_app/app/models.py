from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User


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


class Article(models.Model):
    title = models.CharField("Название поста", max_length=150)
    content = models.TextField("Описание поста")
    image = models.ImageField("Фотка поста", upload_to="photos/", null=True, blank=True)
    created_at = models.DateTimeField("Дата создания поста", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления поста", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор поста")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория поста")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]

