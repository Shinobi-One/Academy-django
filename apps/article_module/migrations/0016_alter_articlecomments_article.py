# Generated by Django 3.2.20 on 2023-07-12 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0015_alter_article_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='article_module.article', verbose_name='مقاله'),
        ),
    ]