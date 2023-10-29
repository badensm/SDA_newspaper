from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, permissions, filters
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from .paginators import ArticlePaginator
# Create your views here.

class ListCreateArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePaginator
    filter_backends = [filters.OrderingFilter]
    ordering = ['-create_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

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

class APIroot(APIView):
    def get(self, request, format=None):
        links = {
            'users': reverse('users', request=request, format=format),
            'articles': reverse('articles', request=request, format=format)
        }
        return Response(links)
  
