# Generated by Django 4.0.3 on 2022-04-26 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_rename_total_leaves_leaves_remaining_leaves'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaves',
            old_name='remaining_leaves',
            new_name='total_leaves',
        ),
    ]
