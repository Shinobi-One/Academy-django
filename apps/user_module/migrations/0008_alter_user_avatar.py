# Generated by Django 3.2.20 on 2023-07-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0007_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='آواتار'),
        ),
    ]
