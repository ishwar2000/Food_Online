# Generated by Django 5.0.2 on 2024-04-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_cover_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_profile',
            field=models.ImageField(blank=True, null=True, upload_to='static/user/cover_profile_picture/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/user/profile_picture/'),
        ),
    ]
