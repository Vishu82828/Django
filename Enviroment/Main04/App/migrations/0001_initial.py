# Generated by Django 5.1.4 on 2025-01-16 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('bg_color', models.CharField(choices=[('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='App.profile')),
            ],
        ),
    ]
