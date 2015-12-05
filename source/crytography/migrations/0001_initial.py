# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('message', models.TextField()),
                ('encrypted_message', models.CharField(max_length=200)),
                ('hashed_message', models.CharField(max_length=100)),
                ('user_name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
