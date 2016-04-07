from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Album, Musician
from .forms import AlbumFormSet, MusicianForm

class MusicianList(ListView):
        model = Musician
        context_object_name = 'musicians'


class MusicianDetail(DetailView):

    model = Musician

    def get_context_data(self, **kwargs):
        # We grab the variable pk from the urlpattern
        artist_id = self.kwargs['pk']

        # Call the base implementation first to get a context
        context = super(MusicianDetail, self).get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(artist_id=artist_id)

        return context


def musician_create(request, template='demoapp/musician_new.html'):

    if request.method == 'POST':
        musician = MusicianForm(request.POST)
        album = AlbumFormSet(request.POST, instance=Musician())

        if musician.is_valid():
            musician = musician.save(commit=False)
            album = AlbumFormSet(request.POST, instance=musician)

            if album.is_valid():
                musician.save()
                album.save()
            return HttpResponseRedirect('/success/')

    # It's not a post, so render the blank form.
    else:
        musician = MusicianForm()
        album = AlbumFormSet(instance=Musician())

    return render(request, template, {'musician': musician,
        'albums': album
    })
