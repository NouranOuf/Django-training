# Generated by Django 4.1.2 on 2022-10-12 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0012_remove_album_creation_day_album_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='approved_albums',
            field=models.BooleanField(default=False, help_text='Approve the album if its name is not explicit'),
        ),
        migrations.AlterField(
            model_name='album',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 21, 46, 10, 223054, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 21, 46, 10, 223054, tzinfo=datetime.timezone.utc)),
        ),
    ]