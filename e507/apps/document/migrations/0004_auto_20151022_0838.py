# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_auto_20151013_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='style',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
