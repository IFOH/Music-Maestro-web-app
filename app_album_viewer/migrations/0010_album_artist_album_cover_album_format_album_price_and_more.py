# Generated by Django 4.2.5 on 2023-12-04 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_album_viewer', '0009_alter_userprofile_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(default='Artist', max_length=255),
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='album',
            name='format',
            field=models.CharField(choices=[('DD', 'Digital download'), ('CD', 'CD'), ('VN', 'Vinyl')], default='DD', max_length=2),
        ),
        migrations.AddField(
            model_name='album',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.date(2023, 12, 4)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(default='Album title', max_length=255),
        ),
    ]
