from django.db import models

<<<<<<< HEAD
class Host(models.Model):
=======
# update
class Heeler(models.Model):
    bssid = models.CharField(max_length=32)
    frequency = models.CharField(max_length=32)
    ssid = models.CharField(max_length=32)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("ssid",)

    def __repr__(self):
        return self.ssid

    def __str__(self):
        return self.ssid

class Personality(models.Model):
>>>>>>> b3faa8a116bf8c0421a5879130463a4688c0f5af
    id = models.BigAutoField(primary_key = True)
 
    crate_id = models.IntegerField()
    crate_location = models.CharField(max_length=32)
    crate_name = models.CharField(max_length=32)

    def __repr__(self):
        return f"{self.id} {self.crate_id} {self.crate_location} {self.crate_name}"

    def __str__(self):
        return f"{self.id} {self.crate_id} {self.crate_location} {self.crate_name}"

