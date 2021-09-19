from django.shortcuts import render
from .models import Umowy


# Create your views here.
def wszystkie_umowy(request):
    # return HttpResponse('<h1>to jest test aplikacji</h1>')
    wszystkie = Umowy.object.all()

    return render(request, 'ewidencja.html', {'test1': wszystkie})
