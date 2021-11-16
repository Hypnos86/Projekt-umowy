"""umowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from umowyapp.views import wszystkie_umowy, archiwalne_umowy, nowe_umowy, edytuj_umowe, usun_umowe, podglad_umow

urlpatterns = [
    path('', wszystkie_umowy, name="wszystkie_umowy"),
    path('archiwum/', archiwalne_umowy, name="archiwalne_umowy"),
    path('umowa_form/', nowe_umowy, name="nowe_umowy"),
    path('edytuj/<int:id>/', edytuj_umowe, name="edytuj_umowe"),
    path('usun/<int:id>/', usun_umowe, name="usun_umowe"),
    path('podglad/<int:id>/', podglad_umow, name="podglad_umowy"),
]
