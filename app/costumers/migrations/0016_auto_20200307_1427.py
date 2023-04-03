# Generated by Django 2.2 on 2020-03-07 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
        ('costumers', '0015_auto_20200307_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinvoice',
            name='charges_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='επιβαρυνσεις'),
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='charges_taxes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='επιβαρυνσεις ΦΠΑ'),
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='final_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Τελική Αξία'),
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='payment_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PaymentMethod'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='clean_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Καθαρη Αξια'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='discount_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Εκπτωση'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='taxes_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Συνολο ΦΠΑ'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='total_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=17, verbose_name='Πληρωτεο Ποσο'),
        ),
    ]