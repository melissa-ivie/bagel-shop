# Generated by Django 3.0.3 on 2020-10-20 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0008_auto_20201020_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='associated_line_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bagel_site.LineItem'),
        ),
    ]
