from django.db import models

class Heeler(models.Model):
    bssid = models.CharField(max_length=32)
    frequency_mhz = models.IntegerField()
    signal_dbm = models.IntegerField()
    ssid = models.CharField(max_length=32)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_tablespace = 'wombat_v1'
        ordering = ("ssid",)

    def __repr__(self):
        return self.ssid

    def __str__(self):
        return self.ssid

class Host(models.Model):
    id = models.BigAutoField(primary_key = True)
 
    crate_id = models.IntegerField()
    crate_location = models.CharField(max_length=32)
    crate_name = models.CharField(max_length=32)

    class Meta:
        db_tablespace = 'wombat_v1'

    def __repr__(self):
        return f"{self.id} {self.crate_id} {self.crate_location} {self.crate_name}"

    def __str__(self):
        return f"{self.id} {self.crate_id} {self.crate_location} {self.crate_name}"
