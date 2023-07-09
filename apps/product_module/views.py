from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View
from apps.website_module.models import SiteBanner
from .models import Product, ProductCategory ,ProductBrand,ProductGallery
from ..user_module.models import User
from utils.list_slicers import list_group


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'product'
    ordering = ['-price']
    paginate_by = 5

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        this_category = self.kwargs.get('category')
        this_brand = self.kwargs.get("brand")
        base_query = base_query.filter(is_active=True)
        if this_category is not None :
            base_query = base_query.filter(category__url_title__iexact=this_category)
        if this_brand is not None :
            base_query = base_query.filter(brand__url__iexact=this_brand)
        return base_query

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['top_banner'] = SiteBanner.objects.filter(is_active=True,position__exact=SiteBanner.BannerPosition.product_list_top).first()
        context['right_banner'] = SiteBanner.objects.filter(is_active=True,position__exact=SiteBanner.BannerPosition.product_list_right).first()
        return context
class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # request = self.request
        context = super(ProductDetailView, self).get_context_data()
        # object = self.object.id
        # data = request.session['product']
        # context['stmt'] = data == object
        product : Product = kwargs.get('object')
        context["user"] = User.objects.filter(is_active=True).first()
        product_gallery = ProductGallery.objects.filter(slider_id=product.id)
        context['product_gallery'] = list_group(product_gallery ,3)
        return context

def category_components(request):
    main_categories = ProductCategory.objects.prefetch_related('sub_category').filter(is_active=True,parent = None)
    context = {
        "main_categories" : main_categories
    }
    return render(request, "product_module/components/category_components.html", context)


def brand_components(request ):
    product_brands = ProductBrand.objects.annotate(product_counts=Count('brand')).filter(is_active=True)
    context = {
        "brands" : product_brands
    }
    return render(request, 'product_module/components/product_brand.html',context)
class AddFavorite(View):
    template_name = 'product_module/product_detail.html'
    model = Product

    def post(self, request):
        x = request.POST['product']
        request.session['mahsool'] = x
        return redirect(reverse('shop:product_list'))
