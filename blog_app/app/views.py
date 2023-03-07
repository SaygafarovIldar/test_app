from django.shortcuts import render
from app.models import Category, Article
from .forms import LoginForm

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


def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug).first()
    context = {
        "post": article
    }
    return render(request, "pages/detail.html", context)


def login_view(request):
    form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "pages/login.html", context)


def registration_view(request):
    return render(request, "pages/registration.html")
