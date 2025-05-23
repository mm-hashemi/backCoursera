# Generated by Django 5.2 on 2025-04-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Instructor', 'Instructor'), ('Admin', 'Admin')], default='Student', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Suspended', 'Suspended'), ('Banned', 'Banned')], default='Active', max_length=20),
        ),
    ]
