from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('faqs/', views.Faqs.as_view(), name='faqs'),
    path('privacy_policy/', views.PrivacyPolicy.as_view(), name='privacy_policy'),
    path('terms_of_use/', views.TermsOfUse.as_view(), name='terms_of_use'),
]
