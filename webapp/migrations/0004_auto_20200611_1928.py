# Generated by Django 3.0 on 2020-06-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_raffleparticipants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RaffleParticipants',
            new_name='RaffleParticipant',
        ),
    ]
