from django.urls import path

from accounts.views import LoginView, LogoutView, RegistrationView, AccountView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('user/<int:pk>', AccountView.as_view(), name='user_info'),
]
