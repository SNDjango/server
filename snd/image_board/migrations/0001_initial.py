# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 09:40
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContentHashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ContentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='no title', max_length=100)),
                ('description', models.CharField(default='no description', max_length=400)),
                ('image', models.ImageField(default='null', upload_to='image_board/posts/')),
                ('uploaded_by', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.ContentItem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_text', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.ContentItem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.TextField(blank=True)),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('expertise', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+123456'. Between 5 and 15 digits allowed.", regex='^\\+?1?\\d{5,15}$')])),
                ('contact_skype', models.URLField(blank=True, null=True)),
                ('contact_facebook', models.URLField(blank=True, null=True)),
                ('contact_linkedin', models.URLField(blank=True, null=True)),
                ('user_photo', models.ImageField(default='../media/img/anon.png', upload_to='../media/img')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=150, unique=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('top', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='image_board.ContentItem')),
            ],
        ),
        migrations.CreateModel(
            name='ContentBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.Board')),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.ContentItem')),
            ],
        ),
        migrations.CreateModel(
            name='SubBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contenthashtag',
            name='content_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.ContentItem'),
        ),
        migrations.AddField(
            model_name='contenthashtag',
            name='hashtag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.Hashtag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='contentItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_board.ContentItem'),
        ),
    ]
