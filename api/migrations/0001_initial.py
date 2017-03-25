# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djsessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostedsession', models.CharField(default=b'NULL', max_length=250)),
                ('member', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='finalplaylist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.CharField(default=b'NULL', max_length=250)),
                ('hostedsession', models.ForeignKey(to='api.djsessions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='hostsong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song', models.CharField(default=b'NULL', max_length=250)),
                ('counter', models.CharField(default=b'0', max_length=250)),
                ('hostedsession', models.ForeignKey(to='api.djsessions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(default=b'NULL', max_length=250)),
                ('hotspot', models.CharField(default=b'NULL', max_length=250)),
                ('access_token', models.CharField(default=b'NULL', max_length=250)),
                ('playid', models.CharField(default=b'NULL', max_length=250)),
                ('playurl', models.CharField(default=b'NULplayL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='finalplaylist',
            name='hostname',
            field=models.ForeignKey(to='api.user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='djsessions',
            name='hostname',
            field=models.ForeignKey(to='api.user'),
            preserve_default=True,
        ),
    ]
