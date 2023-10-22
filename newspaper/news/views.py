from django.shortcuts import render
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse({'articles':serializer.data})