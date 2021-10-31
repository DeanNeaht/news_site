from rest_framework import serializers

from accounts.models import User
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = News
        exclude = ('photo',)


class NewsAddSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = News
        fields = ['title', 'text', 'photo', 'author', 'category']

