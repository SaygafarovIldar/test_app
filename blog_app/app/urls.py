from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("category/<slug:category_slug>/", views.category_articles, name="category_articles"),
    path("articles/<slug:article_slug>/", views.article_detail, name="article_detail")
]
