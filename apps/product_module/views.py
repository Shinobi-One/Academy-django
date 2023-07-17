from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View
from apps.website_module.models import SiteBanner
from .models import Product, ProductCategory, ProductBrand, ProductGallery, ProductVisitCount
from ..user_module.models import User
from utils.list_slicers import list_group
from utils.http_serviecs import get_ip

# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'product'
    ordering = ['-price']
    paginate_by = 5

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        request : HttpRequest = self.request
        this_category = self.kwargs.get('category')
        this_brand = self.kwargs.get("brand")
        max_price = request.GET.get('max_price')
        if max_price is not None :
            base_query = base_query.filter(price__lte=max_price)
        min_price =  request.GET.get('min_price')
        print(min_price)
        if min_price is not None :
            base_query = base_query.filter(price__gte=min_price)
        base_query = base_query.filter(is_active=True)
        if this_category is not None:
            base_query = base_query.filter(category__url_title__iexact=this_category)
        if this_brand is not None:
            base_query = base_query.filter(brand__url__iexact=this_brand)
        return base_query

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        request = HttpRequest = self.request
        context['top_banner'] = SiteBanner.objects.filter(is_active=True,
                                                          position__exact=SiteBanner.BannerPosition.product_list_top).first()
        context['right_banner'] = SiteBanner.objects.filter(is_active=True,
                                                           position__exact=SiteBanner.BannerPosition.product_list_right).first()
        query = self.get_queryset()
        max_product : Product = query.order_by('-price').first()
        page_product_maximum_price = max_product.price if max_product is not None else 100000000
        context['page_product_maximum_price'] = page_product_maximum_price
        min_product : Product = query.order_by('price').first()
        page_product_minimum_price = min_product.price if max_product is not  None else 0
        context['page_product_minimum_price'] = page_product_minimum_price
        context['max_price'] = request.GET.get('max_price') or page_product_maximum_price
        context['min_price'] = request.GET.get('min_price') or 0
        return context


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):

        context = super(ProductDetailView, self).get_context_data()
        product : Product = kwargs.get('object')
        category_of_product = list(Product.objects.filter(brand_id=product.brand_id).exclude(pk=product.id).order_by('id')[:9])
        context['related_product'] = list_group(category_of_product, 4)
        context["user"] = User.objects.filter(is_active=True).first()
        product_gallery = list(ProductGallery.objects.filter(slider_id=product.id).all())
        context['product_gallery'] = list_group(product_gallery, 3)
        user_id = None
        user_ip = get_ip(self.request)
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductVisitCount.objects.filter(ip__iexact=user_ip , product_id=product.id,user__exact=user_id).exists()
        if not has_been_visited  :
            new_visit = ProductVisitCount(ip=user_ip,user_id=user_id, product_id=product.id)
            new_visit.save()
        return context


def category_components(request):
    main_categories = ProductCategory.objects.prefetch_related('sub_category').filter(is_active=True, parent=None)
    context = {
        "main_categories": main_categories
    }
    return render(request, "product_module/components/category_components.html", context)


def brand_components(request):
    product_brands = ProductBrand.objects.annotate(product_counts=Count('brand')).filter(is_active=True)
    context = {
        "brands": product_brands
    }
    return render(request, 'product_module/components/product_brand.html', context)


class AddFavorite(View):
    template_name = 'product_module/product_detail.html'
    model = Product

    def post(self, request):
        x = request.POST['product']
        request.session['mahsool'] = x
        return redirect(reverse('shop:product_list'))
