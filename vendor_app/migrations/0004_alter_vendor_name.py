# Generated by Django 5.0 on 2023-12-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0003_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
