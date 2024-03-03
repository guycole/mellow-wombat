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

    def __repr__(self):
        return f"{self.id} {self.adsb_hex} {self.category} {self.flight} {self.model} {self.registration} {self.ladd_flag} {self.military_flag} {self.pia_flag} {self.wierdo_flag}"

    def __str__(self):
        return f"{self.id} {self.adsb_hex} {self.category} {self.flight} {self.model} {self.registration} {self.ladd_flag} {self.military_flag} {self.pia_flag} {self.wierdo_flag}"

#
class AdsbRanking(models.Model):
    id = models.BigAutoField(primary_key = True)

    adsb_hex = models.CharField(max_length=16)
    model = models.CharField(max_length=24)
    population = models.IntegerField()
    rank = models.IntegerField()
    registration = models.CharField(max_length=12)
    score_date = models.DateField()

    def __repr__(self):
        return f"{self.id} {self.adsb_hex} {self.model} {self.population} {self.rank} {self.registration} {self.score_date}"

    def __str__(self):
        return f"{self.id} {self.adsb_hex} {self.model} {self.population} {self.rank} {self.registration} {self.score_date}"

#
class BoxScore(models.Model):
    id = models.BigAutoField(primary_key = True)

    adsb_hex_total = models.IntegerField()
    adsb_hex_new = models.IntegerField()
    device = models.CharField(max_length=32)
    file_population = models.IntegerField()
    refresh_flag = models.BooleanField()
    score_date = models.DateField()

    def __repr__(self):
        return f"{self.id} {self.adsb_hex_total} {self.adsb_hex_new} {self.device} {self.file_population}"

    def __str__(self):
        return f"{self.id} {self.adsb_hex_total} {self.adsb_hex_new} {self.device} {self.file_population}"

#
class Cooked(models.Model):
    id = models.BigAutoField(primary_key = True)

    adsb_hex = models.CharField(max_length=16)
    observed_counter = models.IntegerField()
    observed_first = models.DateTimeField(auto_now_add=True)
    observed_last = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=132)

    def __repr__(self):
        return f"{self.id} {self.adsb_hex} {self.observed_counter} {self.observed_first} {self.observed_last}"

    def __str__(self):
        return f"{self.id} {self.adsb_hex} {self.observed_counter} {self.observed_first} {self.observed_last}"

# 
class Device(models.Model):
    id = models.BigAutoField(primary_key = True)

    altitude = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=32)
    note = models.CharField(max_length=132)
    retired_date = models.DateField()
    start_date = models.DateField()

    def __repr__(self):
        return f"{self.id} {self.name}"

    def __str__(self):
        return f"{self.id} {self.name}"

# file load
class LoadLog(models.Model):
    id = models.BigAutoField(primary_key = True)

    device = models.CharField(max_length=32)
    file_name = models.CharField(max_length=48, unique=True)
    file_type = models.CharField(max_length=16)
    load_time = models.DateTimeField(auto_now_add=True)
    obs_time = models.DateTimeField(auto_now_add=True)
    population = models.IntegerField()

    def __repr__(self):
        return f"{self.id} {self.file_name} {self.load_time} {self.obs_time} {self.population}"

    def __str__(self):
        return f"{self.id} {self.file_name} {self.load_time} {self.obs_time} {self.population}"

# raw data from dump1090
class Observation(models.Model):
    id = models.BigAutoField(primary_key = True)

    adsb_exchange_id = models.IntegerField()
    load_log_id = models.IntegerField()

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
        return f"{self.id} {self.adsb_hex} {self.flight} {self.range} {self.bearing} {self.altitude} {self.speed} {self.track} {self.obs_time}"

    def __str__(self):
        return f"{self.id} {self.adsb_hex} {self.flight} {self.range} {self.bearing} {self.altitude} {self.speed} {self.track} {self.obs_time}"
    
# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
