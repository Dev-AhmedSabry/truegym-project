from rest_framework import generics

from .models import Partner
from .seializers import PartnerSerializer

# Create your views here.

class PartnerListGeneric(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnerOperationGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


