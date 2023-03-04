from django.shortcuts import render
from app.models import Category, Article

# Create your views here.


def home_view(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }

    return render(request, "pages/index.html", context)


def category_articles(request, category_slug):
    category = Category.objects.filter(slug=category_slug).first()
    articles = Article.objects.filter(category=category)
    context = {
        "category": category,
        "articles": articles
    }
    return render(request, "pages/categories.html", context)
