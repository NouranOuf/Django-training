# Generated by Django 4.1.2 on 2022-10-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_remove_artist_approved_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='approved_album',
            field=models.IntegerField(default=0),
        ),
    ]
