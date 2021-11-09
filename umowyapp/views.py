from django.shortcuts import render, get_object_or_404, redirect
from .models import Rodzaje_jednostek, Umowa, Stan_umow
from .forms import UmowyForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def wszystkie_umowy(request):
    # return HttpResponse('<h1>to jest test aplikacji</h1>')
    wszystkie = Umowa.objects.filter(deleted=0)
    archiwalne = Umowa.objects.filter(deleted=1)

    return render(request, 'ewidencja.html', {'wszystkie': wszystkie, 'archiwalne': archiwalne})


@login_required
def archiwalne_umowy(request):
    # return HttpResponse('<h1>to jest test aplikacji</h1>')
    archiwalne = Umowa.objects.filter(deleted=1)
    wszystkie = Umowa.objects.filter(deleted=0)

    return render(request, 'archiwum.html', {'archiwalne': archiwalne, 'wszystkie': wszystkie})


@login_required
def nowe_umowy(request):
    umowa_form = UmowyForm(request.POST or None, request.FILES or None)

    if umowa_form.is_valid():
        umowa_form.save()
        return redirect(wszystkie_umowy)
    return render(request, 'umowa_form.html', {'umowa_form': umowa_form, 'nowy': True})


@login_required
def podglad_umow(request, id):
    podglad = Umowa.objects.get(pk=id)
    form = UmowyForm(request.FILES or None, instance=podglad)
    return render(request, 'podglad.html', {'podglad': podglad})


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
        umowa.deleted = 1
        umowa.stan_umowy = Stan_umow.objects.get(id=2)
        umowa.save()
        return redirect(wszystkie_umowy)
    return render(request, 'usun.html', {'umowa': umowa})

# @login_required
# def szukaj(request):
#     if request.method == "POST":
#         szukane = request.POST['szukane']
#
#         return render(request, 'ewidencja.html', {'szukane': szukane})