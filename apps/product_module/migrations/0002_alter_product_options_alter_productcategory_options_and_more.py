# Generated by Django 4.1.2 on 2023-04-03 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': ' محصول ', 'verbose_name_plural': ' محصول ها '},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'ذسته بندی', 'verbose_name_plural': 'ذسته بندی ها '},
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', verbose_name='توضیحات اصلی'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='فعال / غیر فعال'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(max_length=360, null=True, verbose_name='توضیحات کوتاه'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, verbose_name='عنوان'),
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=300, verbose_name='عنوان')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tag', to='product_module.product', verbose_name='تگ')),
            ],
            options={
                'verbose_name': 'تگ محصول ',
                'verbose_name_plural': 'تگ محصول ها ',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_category', to='product_module.productcategory', verbose_name='دسته بندی'),
        ),
    ]
