from  . import views
from django.urls import path

urlpatterns = [
    path('articles/', views.list_create_articles, name = 'articles'),
    
]
