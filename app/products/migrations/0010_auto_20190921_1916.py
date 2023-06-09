# Generated by Django 2.2.4 on 2019-09-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190921_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_buy',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Αξία Αγορας'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendors',
            field=models.ManyToManyField(blank=True, through='products.ProductVendor', to='vendors.Vendor', verbose_name='Προμηθευτές'),
        ),
    ]
