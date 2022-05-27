from django.db import models

# Create your models here.

class CommonDB(models.Model):
    Id = models.AutoField
    Name = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=200, default="Electronic Product")
    Image1 = models.ImageField(upload_to="SR_Catalogue/images")
    Image2 = models.ImageField(upload_to="SR_Catalogue/images", null=True, blank=True)
    Image3 = models.ImageField(upload_to="SR_Catalogue/images", null=True, blank=True)
    def __str__(self):
        return self.Name
    class Meta:
        abstract=True

class Display(models.Model):
    pathways = (("/remote/0", "Remote"),
                ("/IC_Transistor/0", "IC Transistor"),
                ("/SoundSystem/0", "Sound System"),
                ("/Extension/0", "Extension"),
                ("/DiwaliLights/0", "Diwali Lights"),
                ("/DTH/0", "DTH"),
                ("/Miscellaneous/0", "Miscellaneous"),
                ("/Leads/0", "Leads"),
                ("/LED/0", "LED"),
                ("", "logo"))

    Name=models.CharField(max_length=50, default="")
    Image=models.ImageField(upload_to="SR_Catalogue/images")
    Type_Of_Item=models.CharField(max_length= 30,choices=pathways)

    def __str__(self):
        return self.Name

class Carousel(models.Model):
    Name = models.CharField(max_length=50, default="")
    Image = models.ImageField(upload_to="SR_Catalogue/images")

    def __str__(self):
        return self.Name


class Remote(CommonDB):
    Category = models.CharField(max_length=200, default="Remote")

class IC_Transistor(CommonDB):
    Category = models.CharField(max_length=200, default="IC & Transistors")

class SoundSystem(CommonDB):
    Category = models.CharField(max_length=200, default="Sound System")

class Extension(CommonDB):
    Category = models.CharField(max_length=200, default="Extension")

class Diwali_Light(CommonDB):
    Category = models.CharField(max_length=200, default="Diwali Lights")

class DTH(CommonDB):
    Category = models.CharField(max_length=200, default="DTH")

class Miscellaneous(CommonDB):
    Category = models.CharField(max_length=200, default="Miscellaneous")

class Lead(CommonDB):
    Category = models.CharField(max_length=200, default="Leads")

class LED(CommonDB):
    Category = models.CharField(max_length=200, default="LED")





