from django.shortcuts import render
from .models import *

def index(request):
    disp = Display.objects.all()
    car = Carousel.objects.all()
    params={'Carousel': car, "Display": disp, 'range': range(1, len(car))}
    return render(request, 'Sr_Catalogue/index.html', params)


def Remotes(request):
    rem=Remote.objects.all()
    if len(rem) < 1:
       desc="Sorry, No items available"
       params={'Remotes': rem, "desc": desc, "flag": False}
    else:
        params={'Remotes': rem, "flag": True}
    return render(request, 'Sr_Catalogue/Remote.html', params)

def IC_Transistors(request):
    IC=IC_Transistor.objects.all()
    if len(IC) < 1:
       desc="Sorry, No items available"
       params={'IC': IC, "desc": desc, "flag": False}
    else:
        params={'IC': IC, "flag": True}
    return render(request, 'Sr_Catalogue/IC_Transistor.html', params)

def SoundSystems(request):
    ss=SoundSystem.objects.all()
    if len(ss) < 1:
       desc="Sorry, No items available"
       params = {"Sound": ss, "desc": desc, "flag": False}
    else:
        params={'Sound': ss, "flag": True}
    return render(request, 'Sr_Catalogue/SoundSystem.html', params)

def Extensions(request):
    extension=Extension.objects.all()
    if len(extension) < 1:
       desc="Sorry, No items available"
       params={'Extension': extension, "desc": desc, "flag": False}
    else:
        params={'Extension': extension, "flag": True}
    return render(request, 'Sr_Catalogue/Extension.html', params)

def DiwaliLights(request):
    dl=Diwali_Light.objects.all()
    if len(dl) < 1:
       desc="Sorry, No items available"
       params={'DiwaliLights': dl, "desc": desc, "flag": False}
    else:
        params={'DiwaliLights': dl, "flag": True}
    return render(request, 'Sr_Catalogue/DiwaliLights.html', params)

def DTHs(request):
    dth=DTH.objects.all()
    if len(dth) < 1:
       desc="Sorry, No items available"
       params={'DTH': dth, "desc": desc, "flag": False}
    else:
        params={'DTH': dth, "flag": True}
    return render(request, 'Sr_Catalogue/DTH.html', params)

def Miscellaneouss(request):
    Misc=Miscellaneous.objects.all()
    if len(Misc) < 1:
       desc="Sorry, No items available"
       params={'Miscellaneous': Misc, "desc": desc, "flag": False}
    else:
        params={'Miscellaneous': Misc, "flag": True}
    return render(request, 'Sr_Catalogue/Miscellaneous.html', params)

def Leads(request):
    lead=Lead.objects.all()
    if len(lead) < 1:
        desc = "Sorry, No items available"
        params = {'Leads': lead, "desc": desc, "flag": False}
    else:
        params = {'Leads': lead, "flag": True}
    return render(request, 'Sr_Catalogue/Leads.html', params)

def LEDs(request):
    led=LED.objects.all()
    if len(led) < 1:
        desc = "Sorry, No items available"
        params = {'LED': led, "desc": desc, "flag": False}
    else:
        params = {'LED': led, "flag": True}
    return render(request, 'Sr_Catalogue/LED.html', params)