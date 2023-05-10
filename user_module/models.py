from django.contrib.auth.models import AbstractUser
from django.db import models
from jalali_date import datetime2jalali


# Create your models here.
class User(AbstractUser):
    activation_code = models.CharField(max_length=200, verbose_name='ایمیل فعال سازی')

    class Meta:
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'

    def __str__(self):
        if self.first_name is not  "" and self.last_name is not  "":
            return self.get_full_name()
        return self.email
