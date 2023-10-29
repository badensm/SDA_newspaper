from  . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('articles/', views.ListCreateArticles.as_view(), name = 'articles'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('users/', views.ListCreateUsers.as_view(), name = 'users'),
    path('get-token/',obtain_auth_token),
    path('', views.APIroot.as_view(), name = 'home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
