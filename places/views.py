from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from .forms import PlaceForm
from .models import Place

def home(request):
    places = Place.objects.all()
    return render(request, 'places/home.html')

def places(request):
    places = Place.objects.all()
    return render(request, 'places/places.html', {'places': places})

class PlaceDetailView(DetailView):
    model = Place

@login_required
def newPlace(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('/')
    else:
        form = PlaceForm()
        return render(request, 'places/addplace.html', {'form': form})

@login_required
def editPlace(request, id):
    place = get_object_or_404(Place, pk=id)
    form = PlaceForm(instance=place)

    if(request.method == 'POST'):
        form = PlaceForm(request.POST, instance=place)

        if(form.is_valid()):
            place.save()
            messages.info(request, 'Localidade alterada com sucesso.')
            return redirect('/manage')
        else:
            return render(request, 'places/editplace.html', {'form': form, 'place': place})
    else:
        return render(request, 'places/editplace.html', {'form': form, 'place': place})

def deletePlace(request, id):
    place = get_object_or_404(Place, pk=id)
    place.delete()
    messages.info(request, 'Localidade deletada com sucesso.')

    return redirect('/manage')

def manage(request):
    places = Place.objects.all()
    return render(request, 'places/manage.html', {'places': places})
