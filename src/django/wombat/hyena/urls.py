from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("adsbex_adsb", views.AdsbExViewOrderByAdsb.as_view(), name="adsb_exchange_adsb"),
    path("adsbex_flight", views.AdsbExViewOrderByFlight.as_view(), name="adsb_exchange_flight"),
    path("adsbex_model", views.AdsbExViewOrderByModel.as_view(), name="adsb_exchange_model"),
    path("adsbex_reg", views.AdsbExViewOrderByRegistration.as_view(), name="adsb_exchange_reg"),
    path("obs_adsb", views.ObsViewOrderByAdsb.as_view(), name="obs_adsb"),
    path("obs_flight", views.ObsViewOrderByFlight.as_view(), name="obs_flight"),
    path("obs_time", views.ObsViewOrderByTime.as_view(), name="obs_time"),
]
