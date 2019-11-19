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
            skrypt = "<p>Ryszard Kalisz</p>"
        elif dane == 136:
            skrypt = "<p>Pianista z Jaka to melodia</p>"
        elif dane == 147:
            skrypt ="<p>Łysy z Poranku kojota</p>"
        elif dane == 137:
            skrypt ="<p>Dwayne the Rock Johnson"
        elif dane == 235:
            skrypt = "<p>Macaulay Carson</p>"
        elif dane == 245:
            skrypt = "<p> Joffrey Baretheon</p>"
        elif dane == 246:
            skrypt = "<p>Leo Messi</p>"
        elif dane == 236:
            skrypt = "<p>Robert Lewandowski</p>"
        elif dane == 247:
            skrypt = "<p>Anthony Carrigan</p>"
        elif dane == 237:
            skrypt = "<p>Marcin Gortat</p>"


        return render(request, 'wybierz.html', {'result_present': True, 'skrypt': skrypt})
    return render(request, 'wybierz.html')


def kontakt(request):
    print('skontaktuj się z nami')
    return render(request, 'kontakt.html')


def poznaj(request):
    print('poznaj')
    return render(request, 'poznaj.html')