# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(max_length=100, choices=[(b'Rules', 'Game rules'), (b'Scenarios', 'Scenarios')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='version',
            field=models.CharField(default=b'0.1', max_length=10),
        ),
    ]
