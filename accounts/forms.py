from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

from accounts.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'Пароль'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise ValidationError('Такого пользователя нет')
            if not check_password(password, qs[0].password):
                raise ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'}))
    first_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'}))
    last_name = forms.CharField(label='Ваша фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'}))
    email = forms.CharField(label='Электронная почта', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'Пароль'}))
    password_check = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password_check(self):
        data = self.cleaned_data
        if data.get('password') != data.get('password_check'):
            raise forms.ValidationError('Пароли не совпадают')
        return data.get('password')
