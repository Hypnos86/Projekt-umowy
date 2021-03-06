from django.shortcuts import render, get_object_or_404, redirect
from umowyapp.models import Umowa, Stan_umow, Aneks, Powiaty_Wlkp
from .forms import UmowyForm, AneksForm, PowiatForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def wszystkie_umowy(request):
    wszystkie = Umowa.objects.filter(archiwum=0)
    archiwalne = Umowa.objects.filter(archiwum=1)
    ilosc = len(wszystkie)
    iloscarchi = len(archiwalne)
    q = request.GET.get("q")
    if q:
        wszystkie = wszystkie.filter(miasto_uzyczajacego__icontains=q)
        return render(request, 'ewidencja.html',
                      {'wszystkie': wszystkie, 'archiwalne': archiwalne, 'iloscarchi': iloscarchi, 'ilosc': ilosc,
                       'ewidencja': True})
    else:
        return render(request, 'ewidencja.html',
                      {'wszystkie': wszystkie, 'archiwalne': archiwalne, 'iloscarchi': iloscarchi, 'ilosc': ilosc,
                       'ewidencja': True})


@login_required
def archiwalne_umowy(request):
    archiwalne = Umowa.objects.filter(archiwum=1)
    wszystkie = Umowa.objects.filter(archiwum=0)
    ilosc = len(wszystkie)
    iloscarchi = len(archiwalne)
    q = request.GET.get("q")
    if q:
        archiwalne = archiwalne.filter(miasto_uzyczajacego__icontains=q)
        return render(request, 'ewidencja.html',
                      {'archiwalne': archiwalne, 'wszystkie': wszystkie, 'iloscarchi': iloscarchi, 'ilosc': ilosc,
                       'ewidencja': False})
    else:
        return render(request, 'ewidencja.html',
                      {'archiwalne': archiwalne, 'wszystkie': wszystkie, 'iloscarchi': iloscarchi, 'ilosc': ilosc,
                       'ewidencja': False})


@login_required
def nowe_umowy(request):
    umowa_form = UmowyForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if umowa_form.is_valid():
            instance = umowa_form.save(commit=False)
            instance.autor = request.user
            instance.save()

            return redirect(wszystkie_umowy)

    return render(request, 'umowa_form.html', {'umowa_form': umowa_form, 'nowy': True})


@login_required
def podglad_umow(request, id):
    podglad = Umowa.objects.get(pk=id)
    aneksy = podglad.aneks_set.all()
    return render(request, 'podglad.html', {'podglad': podglad, 'aneksy': aneksy})


@login_required
def edytuj_umowe(request, id):
    umowa_edit = get_object_or_404(Umowa, pk=id)
    umowa_form = UmowyForm(request.POST or None, request.FILES or None, instance=umowa_edit)

    if umowa_form.is_valid():
        umowa_form.save()

        return redirect(wszystkie_umowy)

    return render(request, 'umowa_form.html', {'umowa_form': umowa_form, 'nowy': False})


@login_required
def usun_umowe(request, id):
    umowa = get_object_or_404(Umowa, pk=id)
    if request.method == "POST":
        umowa.archiwum = 1
        umowa.stan_umowy = Stan_umow.objects.get(id=2)
        umowa.save()
        return redirect(wszystkie_umowy)
    return render(request, 'usun.html', {'umowa': umowa})


@login_required
def add_aneks(request):
    aneks_form = AneksForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if aneks_form.is_valid():
            instance = aneks_form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect(wszystkie_umowy)

    return render(request, 'add_aneks.html', {'aneks_form': aneks_form, 'nowy': True})
