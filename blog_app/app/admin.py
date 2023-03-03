from django.contrib import admin
from .models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
