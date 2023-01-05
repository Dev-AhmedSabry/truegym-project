from django.shortcuts import render

from gym.models import Gym

# Create your views here.

def rec_gyms(request):

    rec_gyms = Gym.objects.all()
    context = {'rec_gyms': rec_gyms}
    return render(request, 'home/index.html', context)

def offerd_gyms(request):

    offerd_gyms = Gym.objects.all()
    context = {'offerd_gyms': offerd_gyms}
    return render(request, 'home/index.html', context)

