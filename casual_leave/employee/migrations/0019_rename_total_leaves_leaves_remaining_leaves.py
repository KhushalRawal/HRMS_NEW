# Generated by Django 4.0.3 on 2022-04-26 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_leaves_total_leaves_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaves',
            old_name='total_leaves',
            new_name='remaining_leaves',
        ),
    ]