# Generated by Django 5.0.2 on 2024-02-15 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_watchlist_platform_watchlist_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='platform',
        ),
    ]
