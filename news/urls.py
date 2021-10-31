from django.urls import path

from news.views import NewsView, NewsCreate, NewsDetail, NewsUpdate, NewsDelete, NewsCategoryView

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('add/', NewsCreate.as_view(), name='create_news'),
    path('detail/<int:pk>/', NewsDetail.as_view(), name='detail_news'),
    path('update/<int:pk>/', NewsUpdate.as_view(), name='update_news'),
    path('delete/<int:pk>/', NewsDelete.as_view(), name='delete_news'),
    path('category/<int:pk>/', NewsCategoryView.as_view(), name='category_news'),
]
