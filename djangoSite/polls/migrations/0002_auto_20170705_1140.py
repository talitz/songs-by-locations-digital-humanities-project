# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='cities',
            new_name='song_cities',
        ),
    ]