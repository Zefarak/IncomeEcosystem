# Generated by Django 3.0.1 on 2021-05-28 06:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0044_auto_20210216_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Τηλέφωνο'),
        ),
        migrations.AlterField(
            model_name='paymentinvoice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 6, 57, 42, 153629, tzinfo=utc), verbose_name='Ημερομηνία'),
        ),
    ]