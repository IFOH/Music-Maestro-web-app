# Generated by Django 4.2.5 on 2023-12-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_album_viewer', '0012_alter_album_cover_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(default='sample_data/default-cover.png', upload_to=''),
        ),
    ]
