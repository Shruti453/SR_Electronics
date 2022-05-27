from django.shortcuts import render
from .models import *

def index(request):
    disp = Display.objects.all()
    car = Carousel.objects.all()
    params={'Carousel': car, "Display": disp, 'range': range(1, len(car))}
    return render(request, 'Sr_Catalogue/index.html', params)

def Remotes(request, myid):
    if myid==0:
        rem=Remote.objects.all()
        if len(rem) < 1:
           desc="Sorry, No items available"
           params={'Remotes': rem, "desc": desc, "flag": False}
        else:
            params={'Remotes': rem, "flag": True}
        return render(request, 'Sr_Catalogue/Remote.html', params)
    else:
        rem=Remote.objects.filter(id=myid)
        params={'product': rem[0], 'back': "/remote/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)

def IC_Transistors(request, myid):
    if myid==0:
        IC=IC_Transistor.objects.all()
        if len(IC) < 1:
            desc="Sorry, No items available"
            params={'IC': IC, "desc": desc, "flag": False}
        else:
            params={'IC': IC, "flag": True}
        return render(request, 'Sr_Catalogue/IC_Transistor.html', params)
    else:
        IC=IC_Transistor.objects.filter(id=myid)
        params={'product':IC[0], 'back':"/IC_Transistor/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)


def SoundSystems(request, myid):
    if myid==0:
        ss=SoundSystem.objects.all()
        if len(ss) < 1:
            desc="Sorry, No items available"
            params = {"Sound": ss, "desc": desc, "flag": False}
        else:
            params={'Sound': ss, "flag": True}
        return render(request, 'Sr_Catalogue/SoundSystem.html', params)
    else:
        ss=SoundSystem.objects.filter(id=myid)
        params={'product':ss[0], 'back':"/SoundSystem/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)


def Extensions(request, myid):
    if myid==0:
        extension=Extension.objects.all()
        if len(extension) < 1:
            desc="Sorry, No items available"
            params={'Extension': extension, "desc": desc, "flag": False}
        else:
            params={'Extension': extension, "flag": True}
        return render(request, 'Sr_Catalogue/Extension.html', params)
    else:
        extension=Extension.objects.filter(id=myid)
        params={'product':extension[0], 'back':"/Extension/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)


def DiwaliLights(request, myid):
    if myid==0:
        dl=Diwali_Light.objects.all()
        if len(dl) < 1:
            desc="Sorry, No items available"
            params={'DiwaliLights': dl, "desc": desc, "flag": False}
        else:
            params={'DiwaliLights': dl, "flag": True}
        return render(request, 'Sr_Catalogue/DiwaliLights.html', params)
    else:
        dl=Diwali_Light.objects.filter(id=myid)
        params={'product':dl[0], 'back':"/DiwaliLights/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)


def DTHs(request, myid):
    if myid==0:
        dth=DTH.objects.all()
        if len(dth) < 1:
            desc="Sorry, No items available"
            params={'DTH': dth, "desc": desc, "flag": False}
        else:
            params={'DTH': dth, "flag": True}
        return render(request, 'Sr_Catalogue/DTH.html', params)
    else:
        dth=DTH.objects.filter(id=myid)
        params={'product':dth[0], 'back':"/DTH/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)


def Miscellaneouss(request, myid):
    if myid==0:
        Misc=Miscellaneous.objects.all()
        if len(Misc) < 1:
            desc="Sorry, No items available"
            params={'Miscellaneous': Misc, "desc": desc, "flag": False}
        else:
            params={'Miscellaneous': Misc, "flag": True}
        return render(request, 'Sr_Catalogue/Miscellaneous.html', params)
    else:
        misc=Miscellaneous.objects.filter(id=myid)
        params={'product':misc[0], 'back':"/Miscellaneous/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)

def Leads(request, myid):
    if myid==0:
        lead=Lead.objects.all()
        if len(lead) < 1:
            desc = "Sorry, No items available"
            params = {'Leads': lead, "desc": desc, "flag": False}
        else:
            params = {'Leads': lead, "flag": True}
        return render(request, 'Sr_Catalogue/Leads.html', params)
    else:
        lead=Lead.objects.filter(id=myid)
        params={'product':lead[0], 'back':"/Leads/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)

def LEDs(request, myid):
    if myid==0:
        led=LED.objects.all()
        if len(led) < 1:
            desc = "Sorry, No items available"
            params = {'LED': led, "desc": desc, "flag": False}
        else:
            params = {'LED': led, "flag": True}
        return render(request, 'Sr_Catalogue/LED.html', params)
    else:
        led=LED.objects.filter(id=myid)
        params={'product':led[0], 'back':"/LED/0"}
        return render(request, 'Sr_Catalogue/Product_view.html', params)
