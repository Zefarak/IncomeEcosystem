# Generated by Django 3.0.1 on 2020-03-06 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0010_auto_20200305_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentinvoice',
            name='taxes',
        ),
        migrations.RemoveField(
            model_name='paymentinvoice',
            name='taxes_modifier',
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='clean_value',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=17, verbose_name='Αξια'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Εκπτωση'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='discount_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ποσο Εκπτωσης'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='taxes_modifier',
            field=models.IntegerField(default=24, verbose_name='ΦΠΑ'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='taxes_value',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=17, verbose_name='Αξια ΦΠΑ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='total_clean_value',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=17, verbose_name='Καθαρη Αξια'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='total_value',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=17, verbose_name='Τελικη Αξία'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='discount_value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=17, verbose_name='Εκπτωση'),
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='taxes_value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=17, verbose_name='Συνολο ΦΠΑ'),
        ),
        migrations.AddField(
            model_name='paymentinvoice',
            name='total_value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=17, verbose_name='Πληρωτεο Ποσο'),
        ),
        migrations.AlterField(
            model_name='costumerdetails',
            name='invoice',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='costumers.PaymentInvoice'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='qty',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=17, verbose_name='Ποσότητα'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Περιγραφη'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='unit',
            field=models.CharField(choices=[('a', 'Τεμάχιο'), ('b', 'Κιβώτιο'), ('c', 'Κιλό')], default='a', max_length=1, verbose_name='ΜΜ'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='value',
            field=models.DecimalField(decimal_places=3, max_digits=17, verbose_name='Τιμή'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='clean_value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=17, verbose_name='Καθαρη Αξια'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='value',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=17, verbose_name='Αξια Προ Εκπτωσεως'),
        ),
    ]