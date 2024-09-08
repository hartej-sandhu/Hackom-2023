from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('login', views.loginn, name='login'),
    path('register', views.register, name='Register'), 
    path('onboarding', views.onboarding, name='onboarding'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('outstation', views.outstationn, name='outstation'),
    path('create_outstation', views.create_outstation, name='create_outstation'),
    path('landingPage', views.landingPage, name='landingPage'),
    path('ecoRoute', views.ecoRoute, name='ecoRoute'),
    path('ecoTransit', views.EcoTransit, name='ecoTransit'),
    path('outstation/<id>', views.outstation_detail , name='outstation_detail'),
    path('logout', views.logoutt, name='logout'),
    path('findPool', views.findPool, name='FindPool'),
]
