from django.db import models

# Create your models here.
POWIAT = [(1, 'Chodzież'), (2, 'Czarnków'), (3, 'Gniezno'), (4, 'Gostyń'), (5, 'Grodzisk'), (6, 'Jarocin'),
          (7, 'Kalisz'), (8, 'Kępno'), (9, 'Koło'), (10, 'Konin'), (11, 'Kościan'), (12, 'Krotoszyn'), (13, 'Leszno'),
          (14, 'Międzychód'), (15, 'Nowy Tomyśl'), (16, 'Oborniki'), (17, 'Ostrów Wlkp.'), (18, 'Ostrzeszów'),
          (19, 'Piła'), (20, 'Pleszew'), (21, 'Poznań'), (22, 'Rawicz'), (23, 'Słupca'), (24, 'Szamotuły'),
          (25, 'Środa Wlkp.'), (26, 'Śrem'), (27, 'Turek'), (28, 'Wągrowiec'), (29, 'Wolsztyn'), (30, 'Września'),
          (31, 'Złotów')]

RODZAJ_JEDNOSTKI = [('kwp', 'KWP'), ('kmp', 'KMP'), ('kpp', 'KPP'), ('kp', 'KP'), ('pp', 'PP'), ('rd', 'RD'),
                    ('inne', 'Inne')]


class Umowy(models.Model):
    data_umowy = models.DateField(blank=True)
    nazwa_uzyczajacego = models.CharField(max_length=30, null=True)
    okres_obowiazywania = models.DateField(null=True)
    # powiat = models.CharField(max_length=11, choices=POWIAT, default='Chodzież')
    rodzaj_jednostki = models.CharField(max_length=4, choices=RODZAJ_JEDNOSTKI, default='--wybierz--')
    adres = models.CharField(max_length=30, null=True)
    miasto = models.CharField(max_length=30, null=True)
    kod_pocztowy = models.CharField(max_length=5, null=True)
    pow_uzyczona = models.FloatField(max_length=4, null=True)
    informacje = models.TextField(default="---Wpisz niezbędne informacje---")
    skan_umowy = models.FileField(upload_to='umowy_pdf', null=True, blank=True)
    stan_umowy = models.BooleanField(null=True, default=True)

    def __str__(self):
        return self.umowa_z_data()

    def umowa_z_data(self):
        return "Umowa z dnia {} z {} dla jednostki {}".format(self.data_umowy, self.nazwa_uzyczajacego, self.miasto)
