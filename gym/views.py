from django.shortcuts import render
from django.db.models import Q

from .models import Gym

# Create your views here.

def gym_list(request):

    gym_list = Gym.objects.all()
    context = {'gyms' : gym_list}
    return render(request, 'gym/gym_list.html', context)


def gym_page(request, id):

    gym_page = Gym.objects.get(id=id)
    context = {'gyms' : gym_page}
    return render(request, 'gym/gym_page.html', context)


def gym_search(request):

    if 'q' in request.GET:
        q = request.GET['q']
        multi = Q(Q(name__icontains=q) | Q(city__icontains=q) | Q(area__icontains=q))
        gym_search = Gym.objects.filter(multi)
    else:
        gym_search = Gym.objects.all()
    context = {'gyms': gym_search}
    return render(request, 'gym/search_results.html', context)
