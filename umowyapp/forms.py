from django.forms import ModelForm
from django.forms import DateInput
from .models import Umowy

class DateField(DateInput):
    input_type = "date"

class UmowyForm(ModelForm):
    class Meta:
        model = Umowy
        fields = ['data_umowy',
                  'nr_umowy',
                  'podstawa_prawna',
                  'nazwa_uzyczajacego',
                  'adres_uzyczajacego',
                  'kod_pocztowy_uzyczajacego',
                  'miasto_uzyczajacego',
                  'okres_obowiazywania',
                  'typ_umowy',
                  'pow_uzyczona',
                  'rodzaj_kosztow_prad',
                  'informacje_prad',
                  'rodzaj_kosztow_gaz',
                  'informacje_gaz',
                  'rodzaj_kosztow_woda',
                  'informacje_woda',
                  'rodzaj_kosztow_co',
                  'informacje_co',
                  'stan_umowy',
                  'powiaty_jedn',
                  'rodzaj_jedn',
                  'adres_jedn',
                  'miasto_jedn',
                  'kod_pocztowy_jedn',
                  'skan_umowy',
                  'uwagi',
                  ]

        labels = {'data_umowy': 'Data umowy',
                  'nr_umowy': 'Numer umowy',
                  'podstawa_prawna': 'Podstawa prawna',
                  'nazwa_uzyczajacego': 'Użyczający',
                  'adres_uzyczajacego': 'Adres',
                  'kod_pocztowy_uzyczajacego': 'Kod pocztowy',
                  'miasto_uzyczajacego': 'Miasto',
                  'okres_obowiazywania': 'Data zakończenia umowy',
                  'typ_umowy': "Typ umowy",
                  'pow_uzyczona': 'Powierzchnia [m2]',
                  'rodzaj_kosztow_prad': 'Prąd',
                  'informacje_prad': 'Info o kosztach - energia elektryczna',
                  'rodzaj_kosztow_gaz': 'Gaz',
                  'informacje_gaz': 'Info o kosztach - gaz',
                  'rodzaj_kosztow_woda': 'Woda',
                  'informacje_woda': 'Info o kosztach - woda',
                  'rodzaj_kosztow_co': 'Centralne ogrzewanie',
                  'informacje_co': 'Info o kosztach - centralne ogrzewanie',
                  'stan_umowy': 'Stan umowy',
                  'powiaty_jedn': 'Powiat',
                  'rodzaj_jedn': 'Rodzaj jednostki',
                  'adres_jedn': 'Adres',
                  'miasto_jedn': 'Miasto',
                  'kod_pocztowy_jedn': 'Kod pocztowy',
                  'skan_umowy': 'Skan umowy',
                  'uwagi': 'Uwagi',
                  }
        widgets = {'data_umowy': DateField()}
