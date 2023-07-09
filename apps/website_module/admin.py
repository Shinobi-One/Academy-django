from django.contrib import admin
from .models import SiteSetting, FooterLinkBox, FooterLink, Sliders, SiteBanner


# Register your models here.

@admin.register(SiteSetting)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteBanner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'position']


admin.site.register(FooterLinkBox)
admin.site.register(FooterLink)
admin.site.register(Sliders)
