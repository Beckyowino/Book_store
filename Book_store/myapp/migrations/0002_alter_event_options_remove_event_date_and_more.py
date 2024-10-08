# Generated by Django 5.0.4 on 2024-09-06 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Scheduling', 'verbose_name_plural': 'Scheduling'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.DateField(default=datetime.date.today, help_text='Day of the event', verbose_name='Day of the event'),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time, help_text='Final time', verbose_name='Final time'),
        ),
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time, help_text='Starting time', verbose_name='Starting time'),
        ),
    ]
