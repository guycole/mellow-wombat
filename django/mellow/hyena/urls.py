from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adsbex_adsb", views.AdsbExViewOrderByAdsb.as_view(), name="adsb_exchange_adsb"),
    path("adsbex_flight", views.AdsbExViewOrderByFlight.as_view(), name="adsb_exchange_flight"),
    path("adsbex_model", views.AdsbExViewOrderByModel.as_view(), name="adsb_exchange_model"),
    path("adsbex_reg", views.AdsbExViewOrderByRegistration.as_view(), name="adsb_exchange_reg"),   
]
