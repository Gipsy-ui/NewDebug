from django.db import models

class Animals(models.Model):
    name = models,models.CharField(("Max_length = 100"), max_length=100)
    Species = models.CharField(("Max_length = 100"), max_length=100)
    age = models.IntegerField()
    discription = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.name
    
class Place(models.Model):
    name = models.CharField(("max_length = 100"), max_length=100)
    location = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.name
    
# Create your models here.
