from django.contrib import admin
from .models import Umowy, Powiaty_Wlkp, Rodzaje_jednostek, Stan_umow

# Register your models here.
admin.site.register(Umowy)
admin.site.register(Powiaty_Wlkp)
admin.site.register(Rodzaje_jednostek)
admin.site.register(Stan_umow)
