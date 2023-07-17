from django.contrib import admin
from .models import Product, ProductCategory, ProductTag, ProductBrand, ProductGallery, ProductVisitCount


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category', 'is_active']
    prepopulated_fields = {'slug': ["title", ]}
    list_display = ('title', 'price', 'is_active', 'is_delete')
    list_editable = ('price', 'is_active')


@admin.register(ProductBrand)
class ProductBrand(admin.ModelAdmin):
    list_display = ['title','is_active']
    prepopulated_fields = {"url" : ["title",] }



@admin.register(ProductVisitCount)
class ProductVisit(admin.ModelAdmin):
    pass
admin.site.register(ProductTag)

admin.site.register(ProductCategory)
admin.site.register(ProductGallery)
admin.site.register(Product, ProductAdmin)

