# Generated by Django 4.2.1 on 2023-05-20 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
        ('crew', '0002_rename_crews_crew'),
        ('maintenance', '0005_maintenanceform_pic_officer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MaintenanceForm',
            new_name='PreventiveMaintenanceWO',
        ),
    ]
