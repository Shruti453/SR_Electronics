from django.db import models

# Create your models here.

class CommonDB(models.Model):
    Id = models.AutoField
    Name = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="Remote")
    Price = models.IntegerField(default=0)
    Quantity = models.IntegerField(default=0)
    Image = models.ImageField(upload_to="SR_Catalogue/images")
    def __str__(self):
        return self.Name
    class Meta:
        abstract=True

class Display(models.Model):
    pathways = (("/remote", "Remote"),
                ("/IC_Transistor", "IC Transistor"),
                ("/SoundSystem", "Sound System"),
                ("/Extension", "Extension"),
                ("/DiwaliLights", "Diwali Lights"),
                ("/DTH", "DTH"),
                ("/Miscellaneous", "Miscellaneous"),
                ("/Leads", "Leads"),
                ("/LED", "LED"))

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
    Category = models.CharField(max_length=50, default="Remote")

class IC_Transistor(CommonDB):
    Category = models.CharField(max_length=50, default="IC & Transistors")

class SoundSystem(CommonDB):
    Category = models.CharField(max_length=50, default="Sound System")

class Extension(CommonDB):
    Category = models.CharField(max_length=50, default="Extension")

class Diwali_Light(CommonDB):
    Category = models.CharField(max_length=50, default="Diwali Lights")

class DTH(CommonDB):
    Category = models.CharField(max_length=50, default="DTH")

class Miscellaneous(CommonDB):
    Category = models.CharField(max_length=50, default="Miscellaneous")

class Lead(CommonDB):
    Category = models.CharField(max_length=50, default="Leads")

class LED(CommonDB):
    Category = models.CharField(max_length=50, default="LED")





