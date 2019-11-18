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
    return render(request, 'wybierz.html')


def kontakt(request):
    print('skontaktuj się z nami')
    return render(request, 'kontakt.html')


def poznaj(request):
    print('poznaj')
    return render(request, 'poznaj.html')
