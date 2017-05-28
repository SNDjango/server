# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 14:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_board', '0014_auto_20170528_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['iim', 'im', 'mpo', 'tif', 'hdf', 'ppm', 'cur', 'jpf', 'png', 'jp2', 'msp', 'flc', 'mpeg', 'icns', 'fli', 'jfif', 'pcx', 'pcd', 'ras', 'jpc', 'jpg', 'bufr', 'mic', 'emf', 'wmf', 'gif', 'sgi', 'bw', 'j2c', 'h5', 'pdf', 'ico', 'mpg', 'fit', 'psd', 'jpx', 'eps', 'pbm', 'jpe', 'ps', 'xbm', 'pgm', 'gbr', 'xpm', 'palm', 'tga', 'rgba', 'fits', 'fpx', 'grib', 'rgb', 'jpeg', 'dcx', 'bmp', 'tiff', 'j2k'])]),
        ),
    ]
