from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from rest_framework.authtoken.models import Token

from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import User
from news.models import News


class LoginView(View):

    def get(self, request):
        form = UserLoginForm()
        _next = request.GET.get('next')
        return render(request, template_name='login.html', context={'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('news')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('news')


class RegistrationView(CreateView):
    model = User
    template_name = 'accounts_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data.get('password'))
        new_user.save()
        return super().form_valid(form)


class AccountView(View):

    def get(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        news = News.objects.filter(author=pk)
        token = Token.objects.get_or_create(user_id=pk)
        return render(request, template_name='account_info.html', context={'user': user,
                                                                           'news': news,
                                                                           'token': token[0].key})
