# Generated by Django 4.1.7 on 2025-01-27 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_websitesettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitesettings',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='websitesettings',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='websitesettings',
            name='linkedin_link',
        ),
        migrations.RemoveField(
            model_name='websitesettings',
            name='twitter_link',
        ),
        migrations.AddField(
            model_name='websitesettings',
            name='social_media_links',
            field=models.JSONField(default=dict),
        ),
    ]
