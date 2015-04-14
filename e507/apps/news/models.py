from django.db import models
from django.conf import settings

import datetime


class News(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    message = models.CharField(max_length=100)
# Use WYSIWYG ASAP    message = RedactorField(verbose_name='Message')
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(null=True, blank=True)
# Maybe later   tag = models.ForeignKey('Tag', null=True, blank=True)
    active = models.BooleanField(default=True)
    language = models.CharField(max_length=20, choices=settings.LANGUAGES, default='fr')

    def __str__(self):
        return self.title
