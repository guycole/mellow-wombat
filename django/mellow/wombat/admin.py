from django.contrib import admin

from .models import GeoLoc
from .models import Inventory
from .models import Tasking

admin.site.register(GeoLoc)
admin.site.register(Inventory)
admin.site.register(Tasking)
