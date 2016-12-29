from __future__ import unicode_literals

from django.db import models


class Passenger(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)
    name = models.CharField(max_length=100)
    profile_pic = models.TextField()
    wallet = models.FloatField(default=0)
    boarding_flag = models.BooleanField(default=False)


class Route(models.Model):
    no_of_stops = models.IntegerField()


class Beacon(models.Model):
    STATUS_ENABLE = 1
    STATUS_DISABLED = 9
    STATUS = (
        (STATUS_ENABLE, 'Enabled'),
        (STATUS_DISABLED, 'Disabled')
        )
    beacon_id = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(choices=STATUS, max_length=20, blank=False, null=False, default=STATUS_ENABLE)

class RouteInfo(models.Model):
    beacon = models.ForeignKey(Beacon)
    route = models.ForeignKey(Route)
    last_know_stop = models.IntegerField(default=0)