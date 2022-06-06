from multiprocessing import context
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

def log(request):
  mydata = Plants.objects.all()
  template = loader.get_template('log.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
    # plant_log = Plants.objects.all()
    # template = loader.get_template('log.html')
    # conxt = {}
    # conxt['Plant'] = [[],[],[]]
    # for i in range(len(plant_log)):
    #         conxt['Plant'][0].append(plant_log[i].name)
    #         conxt['Plant'][1].append(plant_log[i].water_date)
    #         conxt['Plant'][2].append(plant_log[i].fert_date)
    # return HttpResponse(template.render(conxt, request))

def updateplants(request, name):
    Plant = Plants.objects.get(name=name)
    Plant.water_date = datetime.date.today()
    Plant.save()
    return HttpResponseRedirect(reverse(homepage))

def fertplants(request, name):
    Plant = Plants.objects.get(name=name)
    Plant.fert_date = datetime.date.today()
    Plant.save()
    return HttpResponseRedirect(reverse(homepage))

def addplantpage(request):
    template = loader.get_template('addplant.html')
    context = {}
    return HttpResponse(template.render(context, request))

def addplant(request):
    v = request.POST['Name']
    w = request.POST['WaterDays']
    x = request.POST['FertDays']
    y = request.POST['WaterDate']
    z = request.POST['FertDate']
    member = Plants(name=v, water_schedule=w, fert_schedule=x, water_date=y, fert_date=z )
    member.save()
    return HttpResponseRedirect(reverse('addplantpage'))

def delete(request, plant_id):
  member = Plants.objects.get(plant_id=plant_id)
  member.delete()
  return HttpResponseRedirect(reverse('log'))