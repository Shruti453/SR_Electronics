from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("remote/<int:myid>", views.Remotes, name="Remote"),
    path("IC_Transistor/<int:myid>", views.IC_Transistors, name="IC"),
    path("SoundSystem/<int:myid>", views.SoundSystems, name="Sound"),
    path("Extension/<int:myid>", views.Extensions, name="Extension"),
    path("DiwaliLights/<int:myid>", views.DiwaliLights, name="diwaliLights"),
    path("DTH/<int:myid>", views.DTHs, name="DTH"),
    path("Miscellaneous/<int:myid>", views.Miscellaneouss, name="Miscellaneous"),
    path("Leads/<int:myid>", views.Leads, name="Leads"),
    path("LED/<int:myid>", views.LEDs, name="LED"),

]

