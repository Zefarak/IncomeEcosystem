# Generated by Django 2.2 on 2020-01-14 05:59

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['-date_expired']},
        ),
        migrations.AlterField(
            model_name='income',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Μετρητα'),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_expired',
            field=models.DateField(verbose_name='Ημερομηνια'),
        ),
        migrations.AlterField(
            model_name='income',
            name='extra',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Επιπλεον Εσοδα'),
        ),
        migrations.AlterField(
            model_name='income',
            name='logistic_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Λογιστικο Συνολο'),
        ),
        migrations.AlterField(
            model_name='income',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Σημειωσεις'),
        ),
        migrations.AlterField(
            model_name='income',
            name='order_cost',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Συνολο Τιμολογιων'),
        ),
        migrations.AlterField(
            model_name='income',
            name='pos',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Συνολο POS'),
        ),
        migrations.AlterField(
            model_name='income',
            name='sum_z',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Ζ Ημερας'),
        ),
        migrations.AlterField(
            model_name='income',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Πραγματικο Συνολο'),
        ),
    ]