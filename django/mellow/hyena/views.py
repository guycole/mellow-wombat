from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView

from .models import AdsbExchange, Observation

def index(request):
#    return HttpResponse("hyena index")
    latest_observation_list = Observation.objects.order_by("-obs_time")
    template = loader.get_template("hyena/index.html")
    context = {
        "latest_observation_list": latest_observation_list,
    }

    return render(request, "hyena/index.html", context)

class AdsbExViewOrderByAdsb(TemplateView):
    template_name = "hyena/adsbex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adsbex_list"] = AdsbExchange.objects.order_by("adsb_hex")
        return context

class AdsbExViewOrderByFlight(TemplateView):
    template_name = "hyena/adsbex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adsbex_list"] = AdsbExchange.objects.order_by("flight")
        return context

class AdsbExViewOrderByModel(TemplateView):
    template_name = "hyena/adsbex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adsbex_list"] = AdsbExchange.objects.order_by("model")
        return context

class AdsbExViewOrderByRegistration(TemplateView):
    template_name = "hyena/adsbex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adsbex_list"] = AdsbExchange.objects.order_by("registration")
        return context
    