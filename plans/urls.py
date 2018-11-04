from django.urls import path

from . import views

urlpatterns = [
    path('choose_plan/', views.choose_plan, name='choose_plan'),
    path('personal_plan/',views.personal_plan, name='personal_plan'),
    path('family_plan/', views.family_plan, name='family_plan'),
]
