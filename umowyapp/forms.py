from django.forms import ModelForm
from .models import Umowy


class UmowyForm(ModelForm):
    class Meta:
        model = Umowy
        fields = ['data_umowy', 'nazwa_uzyczajacego', 'okres_obowiazywania', 'adres', 'miasto', 'kod_pocztowy',
                  'pow_uzyczona', 'informacje', 'skan_umowy']
