# Generated by Django 3.0.3 on 2020-10-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0013_auto_20201025_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='item_type',
            field=models.IntegerField(default=-1),
        ),
    ]
