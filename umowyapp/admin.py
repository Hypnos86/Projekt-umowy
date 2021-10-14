from django.contrib import admin
from .models import Umowy, Powiaty_Wlkp, Rodzaje_jednostek, Stan_umow, Rodzaj_umowy, Podstawa_prawna, Aneksy

# Register your models here.
# admin.site.register(Umowy)
@admin.register(Umowy)
class UmowyAdmin(admin.ModelAdmin):
    list_filter = ["powiaty_jedn"]
    search_fields = ["nr_umowy"]

admin.site.register(Powiaty_Wlkp)
admin.site.register(Rodzaje_jednostek)
admin.site.register(Stan_umow)
admin.site.register(Rodzaj_umowy)
admin.site.register(Podstawa_prawna)
admin.site.register(Aneksy)
