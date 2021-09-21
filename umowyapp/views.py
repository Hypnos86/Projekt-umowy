from django.shortcuts import render, get_object_or_404, redirect
from .models import Umowy
from .forms import UmowyForm


# Create your views here.
def wszystkie_umowy(request):
    # return HttpResponse('<h1>to jest test aplikacji</h1>')
    wszystkie = Umowy.objects.all()

    return render(request, 'ewidencja.html', {'wszystko': wszystkie})


def nowe_umowy(request):
    form = UmowyForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_umowy)
    return render(request, 'umowa_form.html', {'form': form})


def edytuj_umowe(request, id):
    umowa = get_object_or_404(Umowy, pk=id)

    form = UmowyForm(request.POST or None, request.FILES or None, instance=umowa)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_umowy)
    return render(request, 'umowa_form.html', {'form': form})


def usun_umowe(request, id):
    umowa = get_object_or_404(Umowy, pk=id)
    if request.method == "POST":
        umowa.delete()
        return redirect(wszystkie_umowy)
    return render(request, 'usun.html', {'umowa': umowa})
