from django.shortcuts import render, redirect
from .models import Animals, Place

def index(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "animal":
            animal_name = request.POST.get("animal_name")
            species = request.POST.get("species")
            age = request.POST.get("age")
            description = request.POST.get("description")

            if animal_name and species and age:
                Animals.objects.create(
                    name=animal_name, species=species, age=age, description=description
                )

        elif form_type == "place":
            place_name = request.POST.get("place_name")
            location = request.POST.get("location")
            place_description = request.POST.get("place_description")

            if place_name and location:
                Place.objects.create(
                    name=place_name, location=location, description=place_description
                )

        return redirect("index")

    animals = Animals.objects.all()
    places = Place.objects.all()
    return render(request, "create.html", {"animals": animals, "places": places})
