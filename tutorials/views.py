from django.shortcuts import render
from .models import Tutorial
from django.views.generic import ListView
# Create your views here.

class TutorialView(ListView):
    model = Tutorial
    template_name = 'home.html'
