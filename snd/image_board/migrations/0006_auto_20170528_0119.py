# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0005_auto_20170528_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='UserPicture',
        ),
    ]
