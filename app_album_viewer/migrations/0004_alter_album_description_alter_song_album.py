# Generated by Django 4.2.5 on 2023-11-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_album_viewer', '0003_alter_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(blank=True, null=True, to='app_album_viewer.album'),
        ),
    ]