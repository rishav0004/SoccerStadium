# Generated by Django 4.0.1 on 2022-02-11 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Records', '0003_rename_club_logo_players_clublogo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='ClubLogo',
        ),
    ]
