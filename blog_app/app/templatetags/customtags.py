from django import template

from app.models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag()
def get_active_category(request, category):
    slug_from_request = [item for item in request.path.split("/") if item][-1]
    print(slug_from_request)
    return "active" if slug_from_request == category.slug else ""
