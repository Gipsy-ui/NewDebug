from django.shortcuts import render, redirect

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(f"Creating item with name: {name}")
        
        return redirect('list')

    return render(request, 'create.html') # Don't Include myapp/ in the path
