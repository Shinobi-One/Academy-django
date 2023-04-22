from django.shortcuts import render
from product_module.models import Product
from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = 'hi its a good day'
        return context


def header_component(request):
    return render(request, 'include/site_header_component.html', {})


def footer_component(request):
    return render(request, 'include/site_footer-component.html', {})
