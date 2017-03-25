# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170325_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='p_id',
            new_name='pid',
        ),
    ]
