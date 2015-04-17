# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='language',
            field=models.CharField(default=b'fr', max_length=20, choices=[(b'fr', 'French'), (b'en', 'English'), (b'de', 'German')]),
        ),
    ]
