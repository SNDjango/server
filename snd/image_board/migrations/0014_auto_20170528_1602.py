# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 14:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0013_auto_20170528_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['iim', 'fit', 'flc', 'gbr', 'jpeg', 'tiff', 'xpm', 'fpx', 'emf', 'grib', 'bw', 'jpc', 'jpe', 'rgba', 'mic', 'j2c', 'eps', 'jfif', 'j2k', 'dcx', 'ps', 'pdf', 'png', 'tga', 'fits', 'ras', 'ppm', 'bmp', 'gif', 'h5', 'psd', 'im', 'mpo', 'icns', 'pcd', 'jpf', 'msp', 'jp2', 'xbm', 'cur', 'palm', 'pcx', 'jpx', 'hdf', 'rgb', 'ico', 'pbm', 'fli', 'tif', 'pgm', 'sgi', 'mpeg', 'bufr', 'jpg', 'mpg', 'wmf'])]),
        ),
    ]