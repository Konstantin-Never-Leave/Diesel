# Generated by Django 4.2.3 on 2023-08-14 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0002_alter_vehicledriverperiod_added_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicledriverperiod',
            options={'permissions': [('can_access_vehicle_driver_period', 'Can Access Vehicle Driver Period')]},
        ),
    ]
