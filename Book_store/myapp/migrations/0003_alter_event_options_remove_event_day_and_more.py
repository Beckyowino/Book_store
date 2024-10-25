# Generated by Django 5.0.4 on 2024-09-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_event_options_remove_event_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
        migrations.RemoveField(
            model_name='event',
            name='notes',
        ),
        migrations.AddField(
            model_name='event',
            name='summary',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]