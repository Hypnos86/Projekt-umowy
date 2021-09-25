from django.forms import ModelForm
from .models import Umowy


class UmowyForm(ModelForm):
    class Meta:
        model = Umowy
        fields = ['data_umowy',
                  'nr_umowy',
                  'nazwa_uzyczajacego',
                  'adres_uzyczajacego',
                  'kod_pocztowy_uzyczajacego',
                  'miasto_uzyczajacego',
                  'okres_obowiazywania',
                  'pow_uzyczona',
                  'rodzaj_kosztow_prad',
                  'informacje',
                  'stan_umowy',
                  'powiaty_jedn',
                  'rodzaj_jedn',
                  'adres_jedn',
                  'miasto_jedn',
                  'kod_pocztowy_jedn',
                  'skan_umowy',
                  ]

        labels = {'data_umowy':'Data umowy', 'nr_umowy': 'Nume umowy'}