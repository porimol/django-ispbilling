from __future__ import unicode_literals

from django.db import models

# Internet bundle information
class SpeedBundles(models.Model):
    bundle_name = models.CharField(max_length=100, help_text="Internet package/bundle name. Example : Enterprise")
    bundle_speed = models.CharField(max_length=15, help_text="Internet package/bundle speed(Bandwidth). Example : 2mbps")
    bundle_price = models.FloatField()
    bundle_vat = models.FloatField(help_text="It will convert into percentage(%)")

    # __unicode__ on Python 2
    def __unicode__(self):
        return format(self.bundle_name)

    def __str__(self):
        return  format(self.bundle_name)
