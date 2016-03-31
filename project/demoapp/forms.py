from django import forms
from .models import Album, Musician
from django.forms.models import inlineformset_factory


AlbumFormSet = inlineformset_factory(Musician, Album, fields=['name', 'release_date'], can_delete=False, extra=1)


class MusicianForm(forms.ModelForm):
    artist_name = forms.CharField(label='Artist name', max_length=100,
            widget=forms.TextInput(attrs={'class': 'vTextField', 'placeholder': "Artist's name"}))


    class Meta:
        model = Musician
        fields = ('artist_name',)
