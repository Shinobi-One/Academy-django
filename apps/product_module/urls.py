from django.urls import path
from . import views
app_name = "shop"
urlpatterns = [
    path('product_list', views.ProductListView.as_view(), name='product_list'),
    path('product_list/cat/<str:category>', views.ProductListView.as_view(), name='product_list_by_category'),
    path('product_list/brand/<str:brand>', views.ProductListView.as_view(), name='product_list_by_brand'),
    path('product_list/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]
