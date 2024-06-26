# Generated by Django 5.0.3 on 2024-04-28 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['-appointment_date'], 'verbose_name': 'Schedule', 'verbose_name_plural': 'Schedules'},
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='date_appointment',
            new_name='appointment_date',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='hour_appointment',
            new_name='appointment_time',
        ),
    ]
