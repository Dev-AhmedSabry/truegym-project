from django.shortcuts import render

from .models import Partner

# Create your views here.


def partner_list(request):

    partner_list = Partner.objects.all()
    context = {'partners' : partner_list}
    return render(request, 'partner/partner_list.html', context)

