# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 14:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0015_auto_20170528_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['fpx', 'jpe', 'rgba', 'im', 'icns', 'tga', 'xpm', 'gbr', 'cur', 'jpc', 'h5', 'mpo', 'bw', 'j2k', 'png', 'mpeg', 'jp2', 'pbm', 'flc', 'iim', 'ras', 'eps', 'bufr', 'pgm', 'pdf', 'ps', 'rgb', 'pcd', 'xbm', 'palm', 'fli', 'j2c', 'psd', 'jfif', 'hdf', 'jpx', 'jpeg', 'pcx', 'wmf', 'fits', 'msp', 'bmp', 'mpg', 'ico', 'emf', 'sgi', 'fit', 'gif', 'jpg', 'grib', 'ppm', 'tiff', 'tif', 'jpf', 'mic', 'dcx'])]),
        ),
    ]
