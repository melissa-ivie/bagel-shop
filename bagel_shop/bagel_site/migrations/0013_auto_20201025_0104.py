# Generated by Django 3.0.3 on 2020-10-25 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0012_auto_20201025_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='associated_line_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineitem', to='bagel_site.LineItem'),
        ),
    ]
