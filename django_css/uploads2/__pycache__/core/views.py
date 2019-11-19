from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')


def wybierz(request):
    print('Wybierz')
    if request.method == 'POST':
        print('Form')
        dane=  int(request.POST.get("dane"))
        print(dane)
        if dane == 135:
            skrypt = "<p>Donald Trump</p> <img src=\"/static/img/dt.jpg\""
        elif dane == 145:
            skrypt = "<p>Jarosław Kaczyński</p> <img src=\"/static/img/jk.jpg\""
        elif dane == 146:
            skrypt = "<p>Peter Dinklage</p>"
        return render(request, 'wybierz.html', {'result_present': True, 'skrypt': skrypt})
    return render(request, 'wybierz.html')


def kontakt(request):
    print('skontaktuj się z nami')
    return render(request, 'kontakt.html')


def poznaj(request):
    print('poznaj')
    return render(request, 'poznaj.html')
