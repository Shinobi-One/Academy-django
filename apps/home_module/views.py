from django.shortcuts import render
from apps.product_module.models import Product
from django.views.generic import TemplateView
from apps.website_module.models import SiteSetting, FooterLinkBox,Sliders


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        slider : Sliders =  Sliders.objects.filter(is_active=True)
        context['slider'] = slider
        return context


def header_component(request):
    site_settings : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        "site_setting" : site_settings
    }

    return render(request, 'include/site_header_component.html', context)


def footer_component(request):
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        "site" : SiteSetting.objects.all(),
        "footer_link_boxes" : footer_link_boxes
    }

    return render(request, 'include/site_footer-component.html', context)


class AboutUs_View(TemplateView):
    template_name = "home_module/about-us.html"

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_data'] = setting
        return context