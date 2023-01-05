from django.shortcuts import render

from .models import ContactUs, OurTeam, AboutUs

# Create your views here.

def contact_us(request):

    return render(request, 'contact/contact_us.html')


def our_team(request):

    return render(request, 'contact/our_team.html')


def about_us(request):

    return render(request, 'contact/about_us.html')

    