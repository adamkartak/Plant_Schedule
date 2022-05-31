from re import template
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from hello_plants.models import Plants
# import psycopg2
import datetime

# Create your views here.

def homepage(request):
    dt = datetime.date.today()
    plant = Plants.objects.all()
    template = loader.get_template('index.html')
    list = []
    context = {}
    context['Plants'] = []
    for p in range(len(plant)):
        if dt - plant[p].water_date > datetime.timedelta(days=plant[p].water_schedule):
            context['Plants'].append(plant[p].name)
        else:
            pass
    

    return HttpResponse(template.render(context, request))

def updateplants(request, name):
    Plant = Plants.objects.get(name=name)
    Plant.water_date = datetime.date.today()
    Plant.save()
    return HttpResponseRedirect(reverse(homepage))




