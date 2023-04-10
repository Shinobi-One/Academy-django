import django.views.generic
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import  FormView
from .forms import ContactUsModelForm


# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/'
    prefix = 'contact_form'

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)

