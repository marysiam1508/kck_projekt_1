from django.urls import path
from django.contrib import admin

from uploads2.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('wybierz/', views.wybierz, name='wybierz'),
    path('poznaj/', views.poznaj, name='poznaj'),
    path('contact/', views.kontakt, name='kontakt'),
]
