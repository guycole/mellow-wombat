#
# Title:models.py
# Description:
# Development Environment:OS X 10.15.7/Python 3.9.9/Django 4.0.2
# Author:Guy Cole (guycole at gmail dot com)
#
from django.db import models

# event log
class EventLog(models.Model):
    id = models.BigAutoField(primary_key = True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    slot = models.IntegerField()
    event = models.CharField(max_length=256)

    def __repr__(self):
        return f"{self.id} {self.time_stamp} {self.slot}"

    def __str__(self):
        return f"{self.id} {self.time_stamp} {self.slot}"

# geographic location
class GeoLoc(models.Model):
    id = models.BigAutoField(primary_key = True)
    time_stamp = models.BigIntegerField()
    latitude = models.CharField(max_length=16)
    longitude = models.CharField(max_length=16)

    def __repr__(self):
        return f"{self.id} {self.time_stamp} {self.latitude} {self.longitude}"

    def __str__(self):
        return f"{self.id} {self.time_stamp} {self.latitude} {self.longitude}"

# crate shelf inventory
class ShelfInventory(models.Model):
    id = models.BigAutoField(primary_key = True)
    power = models.BooleanField()
    slot = models.IntegerField()
    shelf_type = models.IntegerField()
    description = models.CharField(max_length=64)

    def __repr__(self):
        return f"{self.id} {self.slot} {self.description}"

    def __str__(self):
        return f"{self.id} {self.slot} {self.description}"

# tasking
class Tasking(models.Model):
    id = models.BigAutoField(primary_key = True)
    time_stamp = models.BigIntegerField()

    def __repr__(self):
        return f"{self.id} {self.time_stamp}"

    def __str__(self):
        return f"{self.id} {self.time_stamp}"


# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***