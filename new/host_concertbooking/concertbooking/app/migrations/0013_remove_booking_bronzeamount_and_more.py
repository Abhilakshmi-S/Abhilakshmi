# Generated by Django 4.2.11 on 2024-05-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_deliverydetails_delete_amount_booking_bronzeamount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bronzeamount',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='goldamount',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='silveramount',
        ),
    ]
