from django.contrib import admin

from apps.shopping_cart_module.models import Order, OrderDetail


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass