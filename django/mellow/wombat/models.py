#
# Title:models.py
# Description:
# Development Environment:OS X 10.15.7/Python 3.9.9/Django 4.0.2
# Author:Guy Cole (guycole at gmail dot com)
#
from django.db import models

class GeoLoc(models.Model):
    id = models.BigAutoField(primary_key = True)
    time_stamp = models.BigIntegerField()
    latitude = models.CharField(max_length=16)
    longitude = models.CharField(max_length=16)

    def __repr__(self):
        return f"{self.id} {self.time_stamp} {self.latitude} {self.longitude}"

    def __str__(self):
        return f"{self.id} {self.time_stamp} {self.latitude} {self.longitude}"

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***