# Generated by Django 3.1 on 2020-08-30 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_numberofpeople'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='checckin',
            new_name='checkin',
        ),
    ]