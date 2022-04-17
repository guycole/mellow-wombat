from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Mellow Wombat")

def gps(request):
    return HttpResponse('gps read')
