from django.contrib import admin
from .models import Product, ProductCategory, ProductTag, ProductBrand, ProductGallery


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    prepopulated_fields = {'slug': ["title", ]}
    list_display = ('title', 'price', 'is_active', 'is_delete')
    list_editable = ('price', 'is_active')


admin.site.register(ProductTag)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductGallery)
admin.site.register(Product, ProductAdmin)

