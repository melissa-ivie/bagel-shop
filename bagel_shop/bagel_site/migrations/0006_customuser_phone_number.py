# Generated by Django 3.0.3 on 2020-10-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0005_auto_20201019_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='00000000000', max_length=11),
        ),
    ]
