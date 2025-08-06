from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrapper, name='scrapper'),
    path('delete', views.clear, name='clear'),
]