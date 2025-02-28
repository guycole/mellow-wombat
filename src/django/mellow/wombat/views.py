from django.http import HttpResponse

from django.shortcuts import render

from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Heeler

def index(request):
    return HttpResponse("mellow wombat crate 3")

class HeelerView(generic.ListView):
    template_name = "wombat/heeler.html"

    context_object_name = "observation_list"

    def get_queryset(self):
        return Heeler.objects.all()

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
