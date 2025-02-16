from django.shortcuts import render, redirect, get_object_or_404
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

def update(request, model_type, id):
    if request.method == "POST":
        if model_type == "animal":
            item = get_object_or_404(Animals, id=id)
            item.name = request.POST.get('name')
            item.species = request.POST.get('species')
            item.age = request.POST.get('age')
            item.description = request.POST.get('description')
        elif model_type == "place":
            item = get_object_or_404(Place, id=id)
            item.name = request.POST.get('name')
            item.location = request.POST.get('location')
            item.description = request.POST.get('description')
        else:
            return render(request, 'error.html', {'message': 'Invalid model type'})

        item.save()
        return redirect('index')

    return redirect('index')
