from django.db import models


# Create your models here.
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class Sliders(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک ')
    url = models.URLField(max_length=500, verbose_name='لینک')
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    short_description = models.CharField(max_length=300, verbose_name="توضیحات اسلایدر ")
    image = models.ImageField(upload_to="slider-images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"


class SiteBanner(models.Model):
    class BannerPosition(models.TextChoices):
        product_list_top = 'product_list_top', "بالای صفحه ی لیست محصولات",
        product_list_right = 'product_list_right', "سمت راست صفحه ی لیست محصولات",
        product_detail = 'product_detail', "صفحه ی جزییات محصولات",
        home_page = 'home_page', 'خانه',
        blog_page = 'blog_page', 'صفحه ی مقالات',
        blog_detail_page = 'blog_detail_page', 'صفحه ی جزییات مقالات',
        about_us_page = 'about_us_page', 'درباره ما',
        contact_us = 'contact_us', 'ارتباط با ما',
        user_panel = 'user_panel', 'پنل کاربری'

    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک ')
    url = models.URLField(max_length=500, verbose_name='لینک')
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    image = models.ImageField(upload_to="banner-images")
    position = models.CharField(max_length=300, choices=BannerPosition.choices , verbose_name='موقعیت بنر های تبلیغاتی')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بنر تبلیغاتی"
        verbose_name_plural = "بنر های تبلیغاتی"
