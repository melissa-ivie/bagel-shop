# Generated by Django 3.0.3 on 2020-10-19 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='ordered', max_length=19),
        ),
    ]