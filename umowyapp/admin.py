from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Umowa, Powiaty_Wlkp, Rodzaje_jednostek, Stan_umow, Rodzaj_umowy, Podstawa_prawna, Aneks


class UmowyResource(resources.ModelResource):
    class Meta:
        model = Umowa


# Register your models here.
# admin.site.register(Umowy)
@admin.register(Umowa)
class UmowyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ["data_umowy", "nr_umowy", "nazwa_uzyczajacego", "powiaty_jedn", "rodzaj_jedn", "miasto_jedn",
                    "stan_umowy", "utworzenie", "zmiana", "archiwum"]
    list_filter = ["powiaty_jedn"]
    search_fields = ["nr_umowy", "nazwa_uzyczajacego", "miasto_jedn"]
    resource_class = UmowyResource


@admin.register(Aneks)
class AneksAdmin(admin.ModelAdmin):
    list_display = ["data_aneksu", "utworzenie", "autor"]


admin.site.register(Powiaty_Wlkp)
admin.site.register(Rodzaje_jednostek)
admin.site.register(Stan_umow)
admin.site.register(Rodzaj_umowy)
admin.site.register(Podstawa_prawna)
