# Generated by Django 5.0 on 2023-12-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0004_alter_vendor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=50),
        ),
    ]
