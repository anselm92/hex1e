# Generated by Django 3.0 on 2020-06-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
    ]
