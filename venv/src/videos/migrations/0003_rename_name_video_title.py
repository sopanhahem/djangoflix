# Generated by Django 4.1.3 on 2022-11-21 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_rename_title_video_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
    ]
