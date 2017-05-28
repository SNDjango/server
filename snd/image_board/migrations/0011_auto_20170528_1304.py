# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 11:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0010_auto_20170528_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, validators=[[{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}]]),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['wmf', 'jpf', 'rgba', 'cur', 'grib', 'fli', 'icns', 'bufr', 'mpg', 'emf', 'mpo', 'ico', 'mpeg', 'tga', 'dcx', 'png', 'hdf', 'tiff', 'jpc', 'j2k', 'eps', 'pbm', 'bmp', 'sgi', 'xpm', 'rgb', 'ps', 'palm', 'fpx', 'jpx', 'msp', 'pgm', 'pcx', 'jpe', 'xbm', 'bw', 'fits', 'j2c', 'psd', 'iim', 'gif', 'gbr', 'jpeg', 'ppm', 'h5', 'jp2', 'jpg', 'im', 'mic', 'tif', 'pdf', 'pcd', 'jfif', 'fit', 'flc', 'ras'])]),
        ),
    ]
