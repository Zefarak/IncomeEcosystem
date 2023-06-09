# Generated by Django 2.2 on 2020-03-05 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0007_paymentinvoice_costumer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='costumers.PaymentInvoice'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='place',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]
