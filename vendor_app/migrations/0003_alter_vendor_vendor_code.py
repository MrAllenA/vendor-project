# Generated by Django 5.0 on 2023-12-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0002_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(blank=True, unique=True),
        ),
    ]