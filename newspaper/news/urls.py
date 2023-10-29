from  . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view(), name = 'articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('users/', views.ListCreateUsers.as_view(), name = 'users'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
