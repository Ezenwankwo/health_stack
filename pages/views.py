from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'page/index.html'


class Faqs(TemplateView):
    template_name = 'page/faqs.html'


class PrivacyPolicy(TemplateView):
    template_name = 'page/privacy_policy.html'


class TermsOfUse(TemplateView):
    template_name = 'page/terms_of_use.html'
