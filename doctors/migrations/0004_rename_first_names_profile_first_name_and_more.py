# Generated by Django 5.0.3 on 2024-04-10 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_delete_doctor_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_names',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_names',
            new_name='last_name',
        ),
    ]