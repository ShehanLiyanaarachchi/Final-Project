# Generated by Django 4.0.6 on 2023-05-25 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_profile_transcript_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='student_id',
        ),
    ]