# Generated by Django 3.0.3 on 2020-10-20 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bagel_site', '0006_customuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_item', models.BooleanField(default=True)),
                ('available', models.IntegerField(default=100)),
                ('max_available', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('containing_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bagel_site.Order')),
                ('menu_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bagel_site.MenuItem')),
            ],
        ),
    ]
