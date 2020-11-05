# Generated by Django 3.0.3 on 2020-10-25 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0011_auto_20201025_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='associated_line_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bagel_site.LineItem'),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bagel_site.MenuItem'),
        ),
    ]
