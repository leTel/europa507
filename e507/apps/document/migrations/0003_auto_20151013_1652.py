# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20151013_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='audience',
            field=models.CharField(max_length=100, choices=[(b'MA', 'Game master'), (b'PL', 'Player')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(max_length=100, choices=[(b'RU', 'Game rules'), (b'SC', 'Scenarios')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='style',
            field=models.CharField(default=b'default_doc.css', max_length=200),
        ),
    ]
