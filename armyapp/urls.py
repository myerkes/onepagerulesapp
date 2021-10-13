from django.urls import path

from . import views

app_name = 'armyapp'
urlpatterns = [
    path('armyapp/index', views.index, name='index'),
]