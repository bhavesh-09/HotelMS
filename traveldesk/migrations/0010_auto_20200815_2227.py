# Generated by Django 3.0.6 on 2020-08-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveldesk', '0009_auto_20200813_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick_drop',
            name='time',
            field=models.CharField(default='', max_length=100),
        ),
    ]
