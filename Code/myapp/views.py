from django.shortcuts import render, redirect
from .models import Animals, Place

def index(request):
    animals = Animals.objects.all()
    places = Place.objects.all()

    return render(request, 'create.html', {"animals": animals, "places": places}) # Don't Include myapp/ in the path
