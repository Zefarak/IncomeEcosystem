# Generated by Django 3.0.1 on 2019-12-23 07:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
            ],
            options={
                'verbose_name_plural': '4. Λογαριασμοί',
            },
        ),
        migrations.CreateModel(
            name='GenericExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Έξοδο',
                'verbose_name_plural': '7. Γενικά Έξοδα',
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=64, verbose_name='Απασχόληση')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Σημειώσεις')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Υπόλοιπο')),
            ],
            options={
                'verbose_name': 'Απασχόληση',
                'verbose_name_plural': '5. Απασχόληση',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Ονοματεπώνυμο')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Τηλέφωνο')),
                ('phone1', models.CharField(blank=True, max_length=10, verbose_name='Κινητό')),
                ('date_added', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία Πρόσληψης')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=50, verbose_name='Υπόλοιπο')),
                ('vacation_days', models.IntegerField(default=0, verbose_name='Συνολικές Μέρες Αδειας')),
                ('occupation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='payroll.Occupation', verbose_name='Απασχόληση')),
            ],
            options={
                'verbose_name': 'Υπάλληλος',
                'verbose_name_plural': '6. Υπάλληλος',
            },
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Friendly ID')),
                ('title', models.CharField(max_length=150, verbose_name='Τίτλος')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Σημειώσεις')),
                ('date_expired', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αξία')),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Φόροι')),
                ('paid_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Πληρωτέο Ποσό')),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Τελική Αξίσ')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Επιπλέον Έκπτωση')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Πληρωμένο?')),
                ('printed', models.BooleanField(default=False, verbose_name='Εκτυπωμένο')),
                ('category', models.CharField(choices=[('1', 'Μισθός'), ('2', 'ΙΚΑ'), ('3', 'ΑΣΦΑΛΙΣΤΙΚΕΣ ΕΙΣΦΟΡΕΣ'), ('4', 'ΗΜΕΡΟΜΗΣΘΙΟ'), ('5', 'ΕΡΓΟΣΗΜΟ'), ('6', 'ΔΩΡΟ')], default='1', max_length=1)),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PaymentMethod', verbose_name='Τρόπος Πληρωμής')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='person_invoices', to='payroll.Person', verbose_name='Υπάλληλος')),
            ],
            options={
                'verbose_name': 'Εντολή Πληρωμής',
                'verbose_name_plural': '2. Μισθόδοσία',
                'ordering': ['is_paid', '-date_expired'],
            },
        ),
        migrations.CreateModel(
            name='GenericExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Friendly ID')),
                ('title', models.CharField(max_length=150, verbose_name='Τίτλος')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Σημειώσεις')),
                ('date_expired', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αξία')),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Φόροι')),
                ('paid_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Πληρωτέο Ποσό')),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Τελική Αξίσ')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Επιπλέον Έκπτωση')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Πληρωμένο?')),
                ('printed', models.BooleanField(default=False, verbose_name='Εκτυπωμένο')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to='payroll.GenericExpenseCategory')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PaymentMethod', verbose_name='Τρόπος Πληρωμής')),
            ],
            options={
                'verbose_name': 'Εντολή Πληρωμής',
                'verbose_name_plural': '3. Εντολή Πληρωμής Γενικών Εξόδων',
                'ordering': ['is_paid', '-date_expired'],
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Friendly ID')),
                ('title', models.CharField(max_length=150, verbose_name='Τίτλος')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Σημειώσεις')),
                ('date_expired', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αξία')),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Φόροι')),
                ('paid_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Πληρωτέο Ποσό')),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Τελική Αξίσ')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Επιπλέον Έκπτωση')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Πληρωμένο?')),
                ('printed', models.BooleanField(default=False, verbose_name='Εκτυπωμένο')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bills', to='payroll.BillCategory', verbose_name='Λογαριασμός')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='frontend.PaymentMethod', verbose_name='Τρόπος Πληρωμής')),
            ],
            options={
                'verbose_name': 'Λογαριασμός',
                'verbose_name_plural': '1. Εντολη Πληρωμης Λογαριασμού',
                'ordering': ['-date_expired'],
            },
        ),
    ]