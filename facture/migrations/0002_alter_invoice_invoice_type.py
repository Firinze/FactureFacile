# Generated by Django 5.1.3 on 2024-12-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('R', 'RECEIPT'), ('P', 'PROFORMA INVOICE'), ('I', 'INVOICE')], max_length=1),
        ),
    ]
