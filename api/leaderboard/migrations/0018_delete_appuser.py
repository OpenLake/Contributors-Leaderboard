# Generated by Django 3.2.4 on 2022-12-31 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0017_appuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AppUser',
        ),
    ]