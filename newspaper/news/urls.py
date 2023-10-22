from  . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view(), name = 'articles'),
    path('articles/<int:article_id>/', views.ArticleDetail.as_view(), name='article_detail'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
