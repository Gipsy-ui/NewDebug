from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Animals, Places  # Ensure correct model names

def index(request):
    animals = Animals.objects.all()
    places = Places.objects.all()
    return render(request, "index.html", {"animals": animals, "places": places})

def save(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "animal":
            try:
                animal = Animals.objects.create(
                    name=request.POST["animal_name"],
                    species=request.POST["species"],
                    age=int(request.POST["age"]),  # Ensure age is an integer
                    description=request.POST.get("description", ""),
                )
                messages.success(request, f"Animal '{animal.name}' added successfully!")
            except Exception as e:
                messages.error(request, f"Error adding animal: {e}")
        
        elif form_type == "place":
            try:
                place = Places.objects.create(
                    name=request.POST["place_name"],
                    location=request.POST["location"],
                    description=request.POST.get("place_description", ""),
                )
                messages.success(request, f"Place '{place.name}' added successfully!")
            except Exception as e:
                messages.error(request, f"Error adding place: {e}")

    return redirect(reverse("index"))  # Redirect using named URL

# Load edit page with pre-filled data
def edit(request, model_type, id):
    print(f"Editing {model_type} with ID {id}")  # Debugging line

    if model_type == "animal":
        item = get_object_or_404(Animals, id=id)
    elif model_type == "place":
        item = get_object_or_404(Places, id=id)
    else:
        messages.error(request, "Invalid model type")
        return redirect(reverse("index"))

    return render(request, "edit.html", {"item": item, "model_type": model_type})

# Update existing animal or place
def update(request, model_type, id):
    if request.method == "POST":
        if model_type == "animal":
            item = get_object_or_404(Animals, id=id)
            item.name = request.POST["name"]
            item.species = request.POST["species"]
            item.age = int(request.POST["age"])  # Ensure age is an integer
            item.description = request.POST.get("description", "")
            messages.success(request, f"Animal '{item.name}' updated successfully!")
        
        elif model_type == "place":
            item = get_object_or_404(Places, id=id)
            item.name = request.POST["name"]
            item.location = request.POST["location"]
            item.description = request.POST.get("description", "")
            messages.success(request, f"Place '{item.name}' updated successfully!")
        
        else:
            messages.error(request, "Invalid model type")
            return redirect(reverse("index"))

        item.save()
    
    return redirect(reverse("index"))

# Delete an animal or place
def delete(request, model_type, id):
    print(f"Deleting {model_type} with ID {id}")  # Debugging line

    if model_type == "animal":
        item = get_object_or_404(Animals, id=id)
    elif model_type == "place":
        item = get_object_or_404(Places, id=id)
    else:
        messages.error(request, "Invalid model type")
        return redirect(reverse("index"))

    item.delete()
    messages.success(request, f"{model_type.capitalize()} '{item.name}' deleted successfully!")
    return redirect(reverse("index"))
