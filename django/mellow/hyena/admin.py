from django.contrib import admin

from .models import AdsbExchange, LoadLog, Observation 

admin.site.register(AdsbExchange)
admin.site.register(LoadLog)
admin.site.register(Observation)
