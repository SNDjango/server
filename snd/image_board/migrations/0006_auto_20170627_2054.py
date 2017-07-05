# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 18:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image_board', '0005_auto_20170627_2038'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together=set([('user_id', 'comment_id')]),
        ),
    ]