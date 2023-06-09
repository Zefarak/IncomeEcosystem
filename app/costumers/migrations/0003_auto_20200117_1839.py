# Generated by Django 2.2.4 on 2020-01-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0002_auto_20190830_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='address',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Διευθυνση'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='afm',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ΑΦΜ'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='destination',
            field=models.CharField(blank=True, default='Εδρα του,', max_length=240, null=True, verbose_name='Προορισμος'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='destination_city',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Πολη'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='doy',
            field=models.CharField(blank=True, default='Σπαρτη', max_length=240, null=True, verbose_name='ΔΟΥ'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='job_description',
            field=models.CharField(blank=True, max_length=240, null=True, verbose_name='Επαγγελμα'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='loading_place',
            field=models.CharField(blank=True, default='Εδρα μας', max_length=240, null=True, verbose_name='Τοπος Φορτωσης'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='transport',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
