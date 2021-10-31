from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import NewsListApi, NewsDetailApi, documentation_view, NewsListCreateApi, NewsDetailUpdateDestroyApi

urlpatterns = [
    path('news/', NewsListApi.as_view(), name='news_api'),
    path('news/<str:category>/', NewsListApi.as_view(), name='news_category_api'),
    path('news/detail/<int:pk>/', NewsDetailApi.as_view(), name='news_detail_api'),
    path('news/user/<str:username>/', NewsListApi.as_view(), name='news_user_api'),
    path('auth/news/', NewsListCreateApi.as_view(), name='news_create_api'),
    path('auth/news/<int:pk>/', NewsDetailUpdateDestroyApi.as_view(), name='news_auth_detail_api'),
    path('', documentation_view, name='documentation'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
