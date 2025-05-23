# Generated by Django 5.2 on 2025-04-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoImage', models.ImageField(upload_to='companies/')),
            ],
        ),
        migrations.CreateModel(
            name='HeroBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='banner/')),
                ('description', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('salary', models.IntegerField(default=0)),
                ('credentials', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='roles/')),
                ('category', models.CharField(max_length=50)),
                ('startDate', models.CharField(max_length=50)),
            ],
        ),
    ]
