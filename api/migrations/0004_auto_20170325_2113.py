# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170325_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pid',
            new_name='playid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='url',
        ),
        migrations.AddField(
            model_name='user',
            name='playurl',
            field=models.CharField(default=b'NULplayL', max_length=250),
            preserve_default=True,
        ),
    ]
