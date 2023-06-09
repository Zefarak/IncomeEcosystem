# Generated by Django 2.2.4 on 2019-09-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190917_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='final_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Αρχική Τιμή Πώλησης'),
        ),
        migrations.AlterField(
            model_name='product',
            name='value_discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Τιμή Έκπτωσης'),
        ),
    ]
