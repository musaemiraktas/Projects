from django.urls import path
from . import views

#http://127.0.0.1:8000/


urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path('search/', views.search_articles, name='search_articles'),
    path('article/<str:filename>/', views.view_article, name='view_article'),
    path('add-interests/', views.add_keywords_to_interests, name='add_interests'),
    path('eject-interests/', views.eject_keywords_to_interests, name = 'eject_interests'),
    path('profile/', views.user_profile, name='user_profile'),
]