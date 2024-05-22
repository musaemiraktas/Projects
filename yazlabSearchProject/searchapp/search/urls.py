from django.urls import path
from . import views
from search.views import download_pdf


# http://127.0.0.1:8000

urlpatterns = [
    path("", views.home, name= "home"),
    path("search/", views.search, name= "search"),
    path('download_pdf/<path:path_to_pdf>/<str:title>/', download_pdf, name='download_pdf'),
    path('article/<path:title>/', views.article_detail, name= 'article_detail'),
]