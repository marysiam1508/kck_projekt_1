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
            skrypt = "<p>Jarosław Kaczyński</p> <img src=\"/static/img/jarek.jpg\""
        elif dane == 146:
            skrypt = "<p>Ryszard Kalisz</p><img src=\"/static/img/kalisz.jpg\""
        elif dane == 136:
            skrypt = "<p>Pianista z Jaka to melodia</p><img src=\"/static/img/osam.jpg\""
        elif dane == 147:
            skrypt ="<p>Jerzy Urban</p><img src=\"/static/img/jerzy-urban.jpeg\""
        elif dane == 137:
            skrypt ="<p>Dwayne Johnson</p><img src=\"/static/img/rock.jpg\""
        elif dane == 235:
            skrypt = "<p>Macaulay Carson</p><img src=\"/static/img/kevin.jpg\""
        elif dane == 245:
            skrypt = "<p> Joffrey Baretheon</p><img src=\"/static/img/jof.jpg\""
        elif dane == 246:
            skrypt = "<p>Harry Potter</p><img src=\"/static/img/hary.jpg\""
        elif dane == 236:
            skrypt = "<p>Robert Lewandowski</p><img src=\"/static/img/lewy.jpg\""
        elif dane == 247:
            skrypt = "<p>dr Konica</p><img src=\"/static/img/lysy.jpg\""
        elif dane == 237:
            skrypt = "<p>Artur Szpilka</p><img src=\"/static/img/szpilka.jpg\""
        else:
            skrypt = "<p>Czyżby zadanie Cię przerosło?</p>"


        return render(request, 'wybierz.html', {'result_present': True, 'skrypt': skrypt})
    return render(request, 'wybierz.html')


def kontakt(request):
    print('skontaktuj się z nami')
    return render(request, 'kontakt.html')


def poznaj(request):
    print('poznaj')
    return render(request, 'poznaj.html')
