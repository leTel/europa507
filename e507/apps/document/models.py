from django.db import models
from django.utils.translation import ugettext_lazy as _

MASTER = "MA"
PLAYER = "PL"

AUDIENCE_CHOICES = (
    (MASTER, _('Game master')),
    (PLAYER, _('Player')),

)

RULES = "RU"
SCENARIOS = "SC"

CATEGORY_CHOICES = (
    (RULES, _('Game rules')),
    (SCENARIOS, _('Scenarios')),
)


class Document(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=200)
    audience = models.CharField(max_length=100, choices=AUDIENCE_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    version = models.CharField(max_length=10, default="0.1")
    template = models.CharField(max_length=200)
    style = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return u"{self.title}".format(**locals())

    def inc_version(self, major_inc=False):
        major = int(self.version.split(".")[0])
        minor = int(self.version.split(".")[1])

        if major_inc:
            major += 1
            minor = 0
        else:
            minor += 1

        self.version("{major}.{minor}".format(**locals()))
        self.save()
        return self.version
