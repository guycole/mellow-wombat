from django.db import models

# adsb_exchange tech
class AdsbExchange(models.Model):
    id = models.BigAutoField(primary_key = True)
  
    adsb_hex = models.CharField(max_length=16)
    category = models.CharField(max_length=8)
    emergency = models.CharField(max_length=8)
    flight = models.CharField(max_length=16)
    model = models.CharField(max_length=24)
    registration = models.CharField(max_length=12)
    ladd_flag = models.BooleanField()
    military_flag = models.BooleanField()
    pia_flag = models.BooleanField()
    wierdo_flag = models.BooleanField()

# file load
class LoadLog(models.Model):
    id = models.BigAutoField(primary_key = True)
    file_name = models.CharField(max_length=48, unique=True)
    load_time = models.DateTimeField(auto_now_add=True)
    obs_time = models.DateTimeField(auto_now_add=True)
    population = models.IntegerField()

# raw data from dump1090
class Observation(models.Model):
    id = models.BigAutoField(primary_key = True)

    adsb_hex = models.CharField(max_length=16)
    altitude = models.IntegerField()
    bearing = models.FloatField()
    flight = models.CharField(max_length=16)
    latitude = models.FloatField()
    longitude = models.FloatField()
    obs_time = models.DateTimeField(auto_now_add=True)
    range = models.FloatField()
    speed = models.IntegerField()
    track = models.IntegerField()

    def __repr__(self):
        return f"{self.id} {self.obs_time} {self.adsb_hex} {self.flight}"

    def __str__(self):
        return f"{self.id} {self.obs_time} {self.adsb_hex} {self.flight}"

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
