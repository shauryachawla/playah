# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Artist'),
        ),
    ]