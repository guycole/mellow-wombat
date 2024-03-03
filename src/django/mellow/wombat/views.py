from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("mellow wombat crate 1")
