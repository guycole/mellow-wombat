from django.db import models

class Personality(models.Model):
    id = models.BigAutoField(primary_key = True)
 
    crate_id = models.IntegerField()
    crate_location = models.CharField(max_length=32)
    crate_name = models.CharField(max_length=32)

    def __repr__(self):
        return f"{self.id} {self.crate_id} {self.crate_location} {self.crate_name}"

    def __str__(self):
        return f"{self.id} {self.crate_id} {self.crate_location} {self.crate_name}"

