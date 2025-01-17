# Generated by Django 4.2 on 2023-05-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_module', '0002_footerlinkbox_footerlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slider_title', models.CharField(max_length=200, verbose_name='عنوان لینک ')),
                ('slider_url', models.URLField(max_length=500, verbose_name='لینک')),
                ('is_active', models.BooleanField(verbose_name='فعتا / غیرفعال')),
                ('short_description', models.CharField(max_length=300, verbose_name='توضیحات اسلایدر ')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]
