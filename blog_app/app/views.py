from django.shortcuts import render
from app.models import Category

# Create your views here.


def home_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, "pages/index.html", context)
