from django.contrib import admin
from django.urls import path
from bbt import views

urlpatterns = [
    path('',views.index,name='bbt'),
    path("about", views.about, name='about'),
    path("tournament", views.tournament, name='tournament'),
    path("contact", views.contact, name='contact'),
    path("register", views.register, name='register'),
]