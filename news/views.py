from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from news.forms import NewsForm
from news.models import News


class NewsView(ListView):
    model = News
    template_name = 'news.html'
    paginate_by = 5

    def get_queryset(self):
        return News.objects.all().select_related('author')


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'


class NewsCreate(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'news_form.html'
    form_class = NewsForm
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'news_update.html'
    form_class = NewsForm


class NewsDelete(LoginRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy('news')
    template_name = 'news_delete.html'


class NewsCategoryView(ListView):
    model = News
    template_name = 'news.html'
    paginate_by = 5
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['pk']).select_related('author')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["cat"] = self.kwargs['pk']
        return data
