# Generated by Django 4.1.2 on 2023-04-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_productbrand_alter_product_slug_alter_product_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300, verbose_name='عنوان')),
            ],
        ),
    ]