# Generated by Django 5.0.3 on 2024-03-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayaw_app', '0008_rename_is_cancel_booking_change_schedule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='change_schedule',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
