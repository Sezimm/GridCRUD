from django.shortcuts import render, redirect
from .forms import EmploeerForm
from .models import Emloeer

def addnew(request):
    if request.method == "POST":
        form = EmploeerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        form = EmploeerForm()
    return render(request, 'drigApp/index.html', {'form': form})
                

def index(request):
    employees = Emloeer.objects.all()
    return render(request, 'drigApp/show.html', {'employees': employees})

def edit(request, id):
    employees = Emloeer.objects.get(id=id)
    return render(request, 'drigApp/edit.html', {'employees': employees})

def update(request, id):
    employees = Emloeer.objects.get(id=id)
    form = EmploeerForm(request.POST, instance=employees)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'drigApp/edit.html', {'employees': employees})

def destroy(request, id):
    employees = Emloeer.objects.get(id=id)
    employees.delete()
    return redirect("/")

