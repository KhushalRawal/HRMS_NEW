# Generated by Django 4.0.3 on 2022-04-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_holidays_remove_leaves_cancel_alter_employee_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidays',
            name='note',
        ),
        migrations.AddField(
            model_name='holidays',
            name='description',
            field=models.TextField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='holidays',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
