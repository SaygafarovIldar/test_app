from django.shortcuts import render
from app.models import Category

# Create your views here.


def home_view(request):
    return render(request, "pages/index.html")


def category_articles(request, category_slug):
    category = Category.objects.filter(slug=category_slug).first()
    context = {
        "category": category
    }
    return render(request, "pages/categories.html", context)
