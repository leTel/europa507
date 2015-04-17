# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150415_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='message',
            field=redactor.fields.RedactorField(verbose_name=b'Message'),
        ),
    ]
