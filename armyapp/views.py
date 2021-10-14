from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from armyapp.models import Army, Unit

# Create your views here.
def index(request):
    #return HttpResponse("Hello world!")
    return render(request, 'armyapp/index.html')

class UnitListView(ListView):
    model = Unit
    context_object_name = 'unit_list'
    queryset = Unit.objects.all
    template_name = 'armyapp/unit_list.html'

class ArmyListview(ListView):
    model = Army
    context_object_name = 'army_list'
    queryset = Army.objects.all
    template_name = 'armyapp/army_list.html'

class ArmyUnitListView(ListView):
    model = Unit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        units = Unit.objects.filter(Army=self.kwargs['army_pk'])
        return context