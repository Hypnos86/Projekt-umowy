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
                  'typ_umowy',
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

        labels = {'data_umowy':'Data umowy',
                  'nr_umowy': 'Numer umowy',
                  'nazwa_uzyczajacego': 'Użyczający',
                  'adres_uzyczajacego': 'Adres',
                  'kod_pocztowy_uzyczajacego': 'Kod pocztowy',
                  'miasto_uzyczajacego': 'Miasto',
                  'okres_obowiazywania': 'Data zakończenia umowy',
                  'typ_umowy': "Typ umowy",
                  'pow_uzyczona': 'Powieżchcnia',
                  'rodzaj_kosztow_prad': 'Prąd',
                  'informacje': 'Info o kosztach',
                  'stan_umowy': 'Stan umowy',
                  'powiaty_jedn': 'Powiat',
                  'rodzaj_jedn': 'Rodzaj jednostki',
                  'adres_jedn': 'Adres',
                  'miasto_jedn': 'Miasto',
                  'kod_pocztowy_jedn': 'Kod pocztowy',
                  'skan_umowy': 'Skan umowy',
                  }