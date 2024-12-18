# Generated by Django 5.1.1 on 2024-10-31 11:33

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_event_options_remove_event_summary_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(11, 33, 18, 55164)),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='Location not specified.', max_length=255),
        ),
    ]
