# Generated by Django 3.0.1 on 2020-12-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0015_auto_20191207_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='identifier',
            field=models.IntegerField(blank=True, null=True, verbose_name='Αριθμος Προϊόντων'),
        ),
    ]
