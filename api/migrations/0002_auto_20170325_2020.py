# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_token',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='p_id',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostsong',
            name='counter',
            field=models.CharField(default=b'0', max_length=250),
        ),
    ]
