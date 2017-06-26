# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-22 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-publication_date']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='contentItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='image_board.ContentItem'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
