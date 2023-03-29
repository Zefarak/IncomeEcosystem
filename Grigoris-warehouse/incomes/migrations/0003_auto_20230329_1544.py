# Generated by Django 3.2.12 on 2023-03-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0002_auto_20200114_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='taxes_13',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 13%'),
        ),
        migrations.AddField(
            model_name='income',
            name='taxes_24',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 24%'),
        ),
        migrations.AddField(
            model_name='income',
            name='taxes_6',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 6%'),
        ),
    ]
