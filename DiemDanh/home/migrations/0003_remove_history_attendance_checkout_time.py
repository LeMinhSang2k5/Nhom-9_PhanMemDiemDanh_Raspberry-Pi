# Generated by Django 5.1.5 on 2025-02-15 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history_attendance',
            name='checkout_time',
        ),
    ]
