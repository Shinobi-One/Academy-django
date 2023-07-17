from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.user_module.models import User


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    parent = models.ForeignKey("ProductCategory", models.CASCADE, blank=True, null=True, related_name="sub_category",
                               verbose_name="دسته بندی والد ")

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="نام برند ")
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    url = models.CharField(max_length=300, verbose_name="برند")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = "برند ها "


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name='دسته بندی ها')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, related_name="brand", verbose_name='برند محصول ',
                              blank=True, null=True)
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='product_image', null=True)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def get_three_digit_prices(self):
        return '{:,}'.format(self.price)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductGallery(models.Model):
    images = models.ImageField(verbose_name="گالری محصولات", blank=True, null=True)
    slider = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_gallery")

    class Meta:
        verbose_name = 'گالری عکس محصول'
        verbose_name_plural = 'گالری عکس محصولات'

    def __str__(self):
        return f"{self.slider.title}"


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption


class ProductVisitCount(models.Model):
    ip = models.CharField(max_length=25, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey('Product', related_name='product_visit', on_delete=models.CASCADE,null=True,blank=True, verbose_name='محصول ')

    def __str__(self):
        return self.ip


    class Meta:
        verbose_name = 'تعداد بازدید محصول '
        verbose_name_plural = 'تعداد بازدید های محصولات'
