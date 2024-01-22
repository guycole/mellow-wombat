from django.db import models

# event log
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
