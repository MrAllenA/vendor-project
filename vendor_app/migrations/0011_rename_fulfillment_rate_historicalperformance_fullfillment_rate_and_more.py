# Generated by Django 5.0 on 2023-12-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0010_alter_historicalperformance_average_response_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalperformance',
            old_name='fulfillment_rate',
            new_name='fullfillment_rate',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fullfillment_rate',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]