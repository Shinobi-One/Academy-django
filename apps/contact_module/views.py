import django.views.generic
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView, CreateView
from .forms import ContactUsModelForm
from apps.website_module.models import SiteSetting

# Create your views here.


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] : SiteSetting =  SiteSetting.objects.filter(is_main_setting=True).first()
        return context


