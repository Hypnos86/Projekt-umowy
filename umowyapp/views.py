from django.shortcuts import render, get_object_or_404, redirect
from .models import Umowy
from .forms import UmowyForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def wszystkie_umowy(request):
    # return HttpResponse('<h1>to jest test aplikacji</h1>')
    wszystkie = Umowy.objects.filter(deleted=0)

    return render(request, 'ewidencja.html', {'wszystko': wszystkie})

@login_required
def nowe_umowy(request):
    form = UmowyForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_umowy)
    return render(request, 'umowa_form.html', {'form': form})

@login_required
def edytuj_umowe(request, id):
    umowa = get_object_or_404(Umowy, pk=id)

    form = UmowyForm(request.POST or None, request.FILES or None, instance=umowa)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_umowy)
    return render(request, 'umowa_form.html', {'form': form})

# @login_required
# def usun_umowe(request, id):
#     umowa = get_object_or_404(Umowy, pk=id)
#     if request.method == "POST":
#         umowa.delete()
#         return redirect(wszystkie_umowy)
#     return render(request, 'usun.html', {'umowa': umowa})
@login_required
def usun_umowe (request, id):
    umowa = get_object_or_404(Umowy, pk=id)
    if request.method =="POST":
        umowa.deleted = 1
        umowa.save()
        return redirect(wszystkie_umowy)
    return render(request, 'usun.html', {'umowa': umowa})