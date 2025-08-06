from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv/<int:id>', views.resume, name='resume'),
    path('cv', views.test, name='test'),
    path('list',views.list,name="list"),
    
]