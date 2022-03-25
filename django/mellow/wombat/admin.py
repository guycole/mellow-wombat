from django.contrib import admin

from .models import EventLog
from .models import GeoLoc
from .models import ShelfInventory
from .models import Tasking

admin.site.register(EventLog)
admin.site.register(GeoLoc)
admin.site.register(ShelfInventory)
admin.site.register(Tasking)
