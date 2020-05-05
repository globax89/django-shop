# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-11 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_auth', '0003_django110'),
    ]

    operations = []

    from django.contrib.auth import validators

    operations.append(
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(
                error_messages={'unique': 'A user with that username already exists.'},
                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                max_length=150,
                unique=True,
                validators=[validators.UnicodeUsernameValidator()],
                verbose_name='username'),
        )
    )
