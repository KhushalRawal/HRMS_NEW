# Generated by Django 4.0.3 on 2022-04-26 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_remove_leave_managment_leaves_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leave_Managment',
            new_name='Leave_Management',
        ),
    ]