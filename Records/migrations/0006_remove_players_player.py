# Generated by Django 4.0.1 on 2022-02-11 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0005_rename_playerid_players_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='Player',
        ),
    ]
