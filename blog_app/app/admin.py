from django.contrib import admin
from .models import Category, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "created_at", "updated_at", "author", "category")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
