# Generated by Django 4.1.2 on 2022-10-12 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_album_approved_albums_alter_album_creation_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='approved_albums',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='creation_day',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 12, 1, 42, 531967, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 12, 1, 42, 531967, tzinfo=datetime.timezone.utc)),
        ),
    ]
