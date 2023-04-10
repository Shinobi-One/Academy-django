from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from .models import Product, ProductCategory


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'product'
    ordering = ['-price']

    def  get_queryset(self):
        base_query = super(ProductListView,self).get_queryset()
        data = base_query.filter(is_active=True)
        return data



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'product'
    # def get_context_data(self, **kwargs):
    #     slug = kwargs['slug']
    #     context = super(ProductDetailView,self).get_context_data()
    #     context['product'] = get_object_or_404(Product, slug=slug)
    #     return context
