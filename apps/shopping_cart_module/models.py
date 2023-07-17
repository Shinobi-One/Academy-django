from django.db import models

from apps.product_module.models import Product
from apps.user_module.models import User


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="کاربر", on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name="پرداخت شده")
    payment_date = models.DateField(null=True, blank=True, verbose_name="زمان پرداخت")


    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش ها"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name="order_products",on_delete=models.CASCADE,verbose_name="سفارش")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product",verbose_name="محصول")
    final_price = models.IntegerField(null=True,blank=True,verbose_name="قیمت نهایی سفارش")
    count = models.IntegerField(verbose_name="تعداد")

    def get_full_price(self):
        return self.product.price * self.count



    def __str__(self):
        return f"سفارش({self.id}) ==> {self.order}"

    class Meta:
        verbose_name = "جزییات سفارش"
        verbose_name_plural = "جزییات سفارش ها"