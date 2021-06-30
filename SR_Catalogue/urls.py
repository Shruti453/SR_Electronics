from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("remote/", views.Remotes, name="Remote"),
    path("IC_Transistor/", views.IC_Transistors, name="IC"),
    path("SoundSystem/", views.SoundSystems, name="Sound"),
    path("Extension/", views.Extensions, name="Extension"),
    path("DiwaliLights/", views.DiwaliLights, name="diwaliLights"),
    path("DTH/", views.DTHs, name="DTH"),
    path("Miscellaneous/", views.Miscellaneouss, name="Miscellaneous"),
    path("Leads/", views.Leads, name="Leads"),
    path("LED/", views.LEDs, name="LED"),

]

