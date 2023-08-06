from django.db.models import Count
from django.shortcuts import render
from apps.product_module.models import Product, ProductCategory ,ProductVisitCount
from django.views.generic import TemplateView
from apps.website_module.models import SiteSetting, FooterLinkBox,Sliders
from utils.list_slicers import list_group

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        slider : Sliders =  Sliders.objects.filter(is_active=True)
        context['slider'] = slider
        latest_products  = Product.objects.filter(is_active=True,is_delete=False).order_by('-id')[:24]
        context['latest_products'] = list_group(latest_products , 4)
        most_viewed = Product.objects.annotate(visit_count=Count('product_visit')).order_by('-visit_count').filter(is_active=True,is_delete=False)[:12]
        context['most_viewed'] = list_group(most_viewed ,4)
        categories = list(ProductCategory.objects.annotate(category_product=Count('product_categories')).filter(is_active=True, is_delete=False,category_product__gt=0).order_by('-parent')[:10])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_categories.all()[:3])
            }
            categories_products.append(item)

        context['categories_products'] = categories_products
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