# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crytography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.ForeignKey(to='crytography.Message')),
                ('user_name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
