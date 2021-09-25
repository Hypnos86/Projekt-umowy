from django.db import models


# Create your models here.
class Powiaty(models.Model):
    powiat = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.powiat_jedn()


    def powiat_jedn(self):
        return "Powiat: {}".format(self.powiat)


class Rodzaj_jednostek(models.Model):
    rodzaj = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.rodzaj_jedn()

    def rodzaj_jedn (self):
        return "{}".format(self.rodzaj)


class Umowy(models.Model):
    data_umowy = models.DateField(blank=True)
    nr_umowy = models.CharField(max_length=15, default="BRAK")
    nazwa_uzyczajacego = models.CharField(max_length=30, null=True)
    adres_uzyczajacego = models.CharField(max_length=30, null=True)
    kod_pocztowy_uzyczajacego = models.CharField(max_length=6, null=True)
    miasto_uzyczajacego = models.CharField(max_length=20, null=True)
    okres_obowiazywania = models.DateField(null=True)
    pow_uzyczona = models.FloatField(max_length=4, null=True)
    rodzaj_kosztow_prad = models.BooleanField(null=True)
    informacje = models.TextField(default="---Niezbędne informacje---")

    # powiaty_jedn = models.OneToOneField(Powiaty, on_delete=models.CASCADE, default=1)
    # rodzaj_jedn = models.OneToOneField(Rodzaj_jednostek, on_delete=models.CASCADE, default=1)

    adres_jedn = models.CharField(max_length=30, null=True)
    miasto_jedn = models.CharField(max_length=20, null=True)
    kod_pocztowy_jedn = models.CharField(max_length=6, null=True)
    skan_umowy = models.FileField(upload_to='umowy_pdf', null=True, blank=True)
    stan_umowy = models.BooleanField(null=True, default=True)
    deleted = models.BooleanField(null=False, default=0)

    def __str__(self):
        return self.umowa_z_data()

    def umowa_z_data(self):
        return "Umowa z dnia {} z {} ".format(self.data_umowy, self.miasto_uzyczajacego)
