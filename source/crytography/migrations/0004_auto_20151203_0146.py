# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crytography', '0003_auto_20151203_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='encrypted_message',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='hashed_message',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
