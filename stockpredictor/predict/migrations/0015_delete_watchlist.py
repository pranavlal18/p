# Generated by Django 4.2.16 on 2024-10-23 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0014_stock_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]