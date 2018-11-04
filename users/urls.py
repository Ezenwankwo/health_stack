from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('register/', views.register, name='register'),
    path('2fa/', views.twofa, name='2fa'),
    path('token/sms', views.token_sms, name='token-sms'),
    path('token/voice', views.token_voice, name='token-voice'),
]
