# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("marksapp", "0006_auto_20170409_1713")]

    operations = [
        migrations.AlterUniqueTogether(name="bookmark", unique_together=set([]))
    ]
