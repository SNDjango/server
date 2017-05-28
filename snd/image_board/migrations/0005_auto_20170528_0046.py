# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0004_user_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentitem',
            name='URL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='contentitem',
            name='publication_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_facebook',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_skype',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_info',
            field=models.TextField(),
        ),
    ]