# Generated by Django 3.0.1 on 2020-03-08 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0023_auto_20200308_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinvoice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 8, 12, 17, 20, 180629, tzinfo=utc), verbose_name='Ημερομηνία'),
        ),
    ]
