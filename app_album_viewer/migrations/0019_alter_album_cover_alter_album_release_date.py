# Generated by Django 4.2.5 on 2023-12-08 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_album_viewer', '0018_alter_album_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(default='default-cover.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.date(2023, 12, 8)),
        ),
    ]