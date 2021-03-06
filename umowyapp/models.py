from django.db import models


# Create your models here.
class Powiaty_Wlkp(models.Model):
    powiat = models.CharField(max_length=12, null=False)

    def __str__(self):
        return f'{self.powiat}'


class Rodzaje_jednostek(models.Model):
    rodzaj = models.CharField(max_length=5, null=False)

    def __str__(self):
        return f'{self.rodzaj}'


class Stan_umow(models.Model):
    stan = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.stan}'


class Rodzaj_umowy(models.Model):
    rodz_um = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rodz_um}'


class Podstawa_prawna(models.Model):
    podstawa = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.podstawa_praw()

    def podstawa_praw(self):
        return "{}".format(self.podstawa)


class Umowa(models.Model):
    data_umowy = models.DateField(null=False)
    nr_umowy = models.CharField(max_length=20, blank=True, default="(BRAK NUMERU)")
    podstawa_prawna = models.ForeignKey(Podstawa_prawna, on_delete=models.CASCADE, blank=True)
    nazwa_uzyczajacego = models.CharField(max_length=30, null=True)
    adres_uzyczajacego = models.CharField(max_length=30, null=True)
    kod_pocztowy_uzyczajacego = models.CharField(max_length=6, null=True)
    miasto_uzyczajacego = models.CharField(max_length=20, null=True)
    okres_obowiazywania = models.DateField(null=True, blank=True)
    typ_umowy = models.ForeignKey(Rodzaj_umowy, on_delete=models.CASCADE)
    pow_uzyczona = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    rodzaj_kosztow_prad = models.BooleanField()
    informacje_prad = models.TextField(blank=True, default="")
    rodzaj_kosztow_gaz = models.BooleanField()
    informacje_gaz = models.TextField(blank=True, default="")
    rodzaj_kosztow_woda = models.BooleanField()
    informacje_woda = models.TextField(blank=True, default="")
    rodzaj_kosztow_co = models.BooleanField()
    informacje_co = models.TextField(blank=True, default="")
    powiaty_jedn = models.ForeignKey(Powiaty_Wlkp, on_delete=models.CASCADE)
    rodzaj_jedn = models.ForeignKey(Rodzaje_jednostek, on_delete=models.CASCADE)
    adres_jedn = models.CharField(max_length=30, null=True)
    miasto_jedn = models.CharField(max_length=20, null=True)
    kod_pocztowy_jedn = models.CharField(max_length=6, null=True)
    skan_umowy = models.FileField(upload_to='umowy_pdf', null=True, blank=True)
    stan_umowy = models.ForeignKey(Stan_umow, on_delete=models.CASCADE, blank=False, default=1)
    uwagi = models.TextField(blank=True, default="")
    archiwum = models.BooleanField(null=False, default=0)
    utworzenie = models.DateTimeField(auto_now_add=True)
    zmiana = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey("auth.User", editable=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'Umowa z dnia {self.data_umowy}, {self.nazwa_uzyczajacego}, {self.miasto_uzyczajacego} (dot.: {self.miasto_jedn})'


class Aneks(models.Model):
    umowa_id = models.ForeignKey("umowyapp.Umowa", on_delete=models.CASCADE)
    skan_aneksu = models.FileField(upload_to='aneksy_pdf/%Y', null=True, blank=True)
    data_aneksu = models.DateField(null=True)
    utworzenie = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data_aneksu} {self.skan_aneksu}'
