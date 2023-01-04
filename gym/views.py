from django.shortcuts import render

from .models import Gym
# Create your views here.

def gym_list(request):

    gym_list = Gym.objects.all()
    context = {'gyms' : gym_list}
    return render(request, 'gym/gym_list.html', context)



def gym_page(request, id):

    gym_page = Gym.objects.get(id=id)
    context = {'gym' : gym_page}
    return render(request, 'gym/gym_page.html', context)


def gym_search(request):

    if request.method == 'POST':
        searched = request.POST['searched']

        return render(request,
        'gym/search_results.html',
        {'searched':searched})

    else:
        return render(request,
        'gym/search_results.html',
        {})

