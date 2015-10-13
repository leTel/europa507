# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('description', models.CharField(max_length=200)),
                ('audience', models.CharField(max_length=100, choices=[(b'Master', 'Game master'), (b'Player', 'Player')])),
                ('category', models.CharField(max_length=100, choices=[(b'Rules', 'Game rules'), (b'Scenario', 'Scenario')])),
                ('version', models.CharField(max_length=10)),
                ('template', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=200)),
            ],
        ),
    ]
