from django.urls import path  # type: ignore
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('getresponse', views.getresponse, name='getresponse')

]