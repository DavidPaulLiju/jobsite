# Generated by Django 5.0.2 on 2024-04-22 02:10

import django.db.models.deletion
import job_listing_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('required_skills', models.CharField(max_length=255)),
                ('employment_type', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('company_logo', models.ImageField(null=True, upload_to=job_listing_app.models.user_directory_path, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_listing_app.job')),
            ],
        ),
    ]
