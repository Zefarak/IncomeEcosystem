# Generated by Django 3.2.7 on 2023-02-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0020_paycheck'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paycheck',
            options={'ordering': ['is_done', 'date']},
        ),
        migrations.AlterField(
            model_name='paycheck',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='ΠΟΣΟ'),
        ),
    ]
