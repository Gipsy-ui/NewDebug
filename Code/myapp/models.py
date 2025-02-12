from django.db import models

class Animals(models.Model):
    name = models.CharField(max_length=100, default="Unknown")  
    species = models.CharField(max_length=100, default="Unknown")  
    age = models.IntegerField()
    description = models.TextField(null=True, blank=True)  

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100, default="Unknown")  
    location = models.CharField(max_length=100, default="Unknown")  
    description = models.TextField(null=True, blank=True)  

    def __str__(self):
        return self.name
