# Generated by Django 3.2.12 on 2023-03-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0021_auto_20230208_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='taxes_13',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 13%'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='taxes_24',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 24%'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='taxes_6',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='ΠΟΣΟ ΦΠΑ 6%'),
        ),
    ]
