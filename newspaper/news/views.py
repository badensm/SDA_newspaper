from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
# Create your views here.

class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # if self.request.method == 'GET':
        #     permission_classes = [permissions.IsAdminUser]
        # else:
        #     permission_classes = [permissions.AllowAny]
        # return [permission() for permission in permission_classes]   
        # permission_classes = [permissions.IsAdminUser] if self.request.method == 'GET' else [permissions.AllowAny]
        # return [permission() for permission in permission_classes]
        return [permissions.IsAdminUser() if self.request.method == 'GET' else permissions.AllowAny()]

  
