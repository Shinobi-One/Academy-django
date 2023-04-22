from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name='شماره همراه')
    activation_email = models.CharField(max_length=200,verbose_name='ایمیل فعال سازی')
    class Meta:
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'