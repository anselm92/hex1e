# Generated by Django 3.0 on 2020-06-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200611_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='raffle',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
