# Generated by Django 3.0.6 on 2020-08-20 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_guest_details',
            name='status',
        ),
    ]