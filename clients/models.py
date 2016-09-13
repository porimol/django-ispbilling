from __future__ import unicode_literals

from django.db import models
from internetbundles.models import SpeedBundles

# Clients/Customers information
class Clients(models.Model):
    first_name = models.CharField(max_length=20, help_text="Customer first name example : Porimol")
    last_name = models.CharField(max_length=20, null=True, help_text="Customer last name example : Chandro")
    nid_number = models.CharField(max_length=60, null=True, verbose_name="NID Number", help_text="Customer national ID card's number.")
    mobile_number = models.CharField(max_length=15, null=True, help_text="Example : 01700000000")
    email_address = models.EmailField(null=True, help_text="Example : email@yourdomain.com")
    present_address = models.TextField()

    class Meta:
        verbose_name = "client information"

    # __unicode__ on Python 2
    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

class ClientUsageBundle(models.Model):
    client = models.ForeignKey(Clients, verbose_name="Client's Name")
    package = models.ForeignKey(SpeedBundles, verbose_name="Speed Bundle")
    subscription_fee = models.FloatField(help_text="Monthly subscription fee")
    service_charge = models.FloatField(help_text="Service/other charge")

    class Meta:
        verbose_name = "client usage package/bundle"

    # __unicode__ on Python 2
    def __unicode__(self):
        return "{0}({1})".format(self.package, self.client)

    def __str__(self):
        return "{0}({1})".format(self.package, self.client)