from django.urls import path

from . import views

app_name = 'armyapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('units/', views.UnitListView.as_view(), name='unitlist'),
    path('armies/', views.ArmyListview.as_view(), name='armylist'),
    path('armies/<int:army_pk>/units', views.ArmyUnitListView.as_view(), name='armyunitlist')

]