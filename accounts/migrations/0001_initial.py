# Generated by Django 5.0.2 on 2024-04-20 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'Customer')], null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_super_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='media/profile_picture/')),
                ('cover_profile', models.ImageField(blank=True, null=True, upload_to='media/profile_picture/')),
                ('address_line_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=6, null=True)),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
