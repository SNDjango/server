# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0003_remove_user_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='image_board.UserPicture'),
            preserve_default=False,
        ),
    ]
