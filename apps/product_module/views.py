from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View

from .models import Product, ProductCategory
from ..user_module.models import User


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'product'
    ordering = ['-price']
    paginate_by = 2

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


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
        context["user"] = User.objects.filter(is_active=True).first()
        return context

def category_components(request):
    main_categories = ProductCategory.objects.filter(is_active=True,parent = None)
    context = {
        "main_categories" : main_categories
    }
    return render(request, "product_module/components/category_components.html", context)
class AddFavorite(View):
    template_name = 'product_module/product_detail.html'
    model = Product

    def post(self, request):
        x = request.POST['product']
        request.session['mahsool'] = x
        return redirect(reverse('shop:product_list'))
