from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from accounts.models import User
from api.permissions import IsOwnerOrReadOnly
from api.serializers import NewsSerializer, NewsAddSerializer
from news.models import News, Category


class NewsListApi(ListAPIView):
    """Возвращает список всех новостей в категории, все новости пользователя или
     если категория не указана возвращает все новости"""
    serializer_class = NewsSerializer
    # permission_classes = (AllowAny,)
    def get_queryset(self):
        category = self.kwargs.get('category')
        user = self.kwargs.get('username')
        if category:
            cat = Category.objects.filter(eng_title=category).first()
            return News.objects.filter(category=cat.pk)
        if user:
            user_pk = User.objects.filter(username=user).first()
            return News.objects.filter(author=user_pk)
        else:
            return News.objects.all()


class NewsDetailApi(RetrieveAPIView):
    """Возвращает конкретную новость"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = (AllowAny,)


class NewsListCreateApi(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsAddSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NewsDetailUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsAddSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (TokenAuthentication,)


def documentation_view(request):
    return render(request, template_name='api_view.html')


