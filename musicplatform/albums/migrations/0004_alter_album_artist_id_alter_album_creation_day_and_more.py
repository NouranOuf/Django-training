# Generated by Django 4.1.2 on 2022-10-07 16:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_remove_artist_social_link_field_artist_social_link_and_more'),
        ('albums', '0003_alter_album_creation_day_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='artists.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='creation_day',
            field=models.DateField(default=datetime.datetime(2022, 10, 7, 16, 30, 6, 881022, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 7, 16, 30, 6, 881022, tzinfo=datetime.timezone.utc)),
        ),
    ]
