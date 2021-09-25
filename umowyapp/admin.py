from django.contrib import admin
from .models import Umowy, Powiaty, Rodzaj_jednostek

# Register your models here.
admin.site.register(Umowy)
admin.site.register(Powiaty)
admin.site.register(Rodzaj_jednostek)
