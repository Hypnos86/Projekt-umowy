from django.db import models


# Create your models here.
class Powiaty_Wlkp(models.Model):
    powiat = models.CharField(max_length=12)

    def __str__(self):
        return self.powiat_jedn()

    def powiat_jedn(self):
        return "{}".format(self.powiat)


class Rodzaje_jednostek(models.Model):
    rodzaj = models.CharField(max_length=4)

    def __str__(self):
        return self.rodzaj_jedn()

    def rodzaj_jedn(self):
        return "{}".format(self.rodzaj)


class Stan_umow(models.Model):
    stan = models.CharField(max_length=14)

    def __str__(self):
        return self.stan_umowy()

    def stan_umowy(self):
        return "{}".format(self.stan)



class Rodzaj_umowy(models.Model):
    rodz_um = models.CharField(max_length=6, null=True)
    
    def __str__(self):
        return self.rodzaj_um()
    
    def rodzaj_um(self):
        return "{}".format(self.rodz_um)


class Umowy(models.Model):
    data_umowy = models.DateField(null=False)
    nr_umowy = models.CharField(max_length=15, null=True, default="BRAK")
    nazwa_uzyczajacego = models.CharField(max_length=30, null=True)
    adres_uzyczajacego = models.CharField(max_length=30, null=True)
    kod_pocztowy_uzyczajacego = models.CharField(max_length=6, null=True)
    miasto_uzyczajacego = models.CharField(max_length=20, null=True)
    okres_obowiazywania = models.DateField(blank=True, default="")
    
    typ_umowy = models.ForeignKey(Rodzaj_umowy, on_delete=models.CASCADE, null=True)
    
    pow_uzyczona = models.FloatField(max_length=4, null=True, blank=True)
    rodzaj_kosztow_prad = models.BooleanField()
    informacje = models.TextField(default="---Niezbędne informacje---")

    powiaty_jedn = models.ForeignKey(Powiaty_Wlkp, on_delete=models.CASCADE)
    rodzaj_jedn = models.ForeignKey(Rodzaje_jednostek, on_delete=models.CASCADE, null=True)

    adres_jedn = models.CharField(max_length=30, null=True)
    miasto_jedn = models.CharField(max_length=20, null=True)
    kod_pocztowy_jedn = models.CharField(max_length=6, null=True)
    skan_umowy = models.FileField(upload_to='umowy_pdf', null=True, blank=True)

    stan_umowy = models.ForeignKey(Stan_umow, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(null=False, default=0)

    def __str__(self):
        return self.umowa_z_data()

    def umowa_z_data(self):
        return "Umowa z dnia {} z {} ({}) - {}. Dotyczy: {} {}".format(self.data_umowy, self.nazwa_uzyczajacego, self.miasto_uzyczajacego, self.typ_umowy, self.rodzaj_jedn, self.miasto_jedn)
