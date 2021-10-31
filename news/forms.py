from django.forms import ModelForm, Textarea, TextInput, ModelChoiceField, ChoiceField
from news.models import News, Category


class NewsForm(ModelForm):

    class Meta:
        model = News
        category = ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория')
        fields = ['title', 'text', 'photo', 'category']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок статьи'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }
