from django.shortcuts import render

from gym.models import Gym

# Create your views here.

def home_page(request):
    return render(request, 'home/index.html')
    pass