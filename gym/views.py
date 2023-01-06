from django.shortcuts import render
from django.db.models import Q
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status, filters, mixins, viewsets
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Gym
from .serializers import GymSerializer
# from .forms import GymSearchForm

# Create your views here.

class GymListGeneric(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','city','area']

class GymOperationGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

# class GymListMixins(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):

#     queryset = Gym.objects.all()
#     serializer_class = GymSerializer

#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)


# @api_view(['GET','POST'])
# def fbv_list(request):

#     if request.method == 'GET':
#         gyms = Gym.objects.all()
#         serializer = GymSerializer(gyms, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = GymSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def fbv_gym_page(request, pk):

#     try:
#         gym = Gym.objects.get(pk=pk)
#     except Gym.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = GymSerializer(gym)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = GymSerializer(gym, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status= status.HTTP_406_NOT_ACCEPTABLE)

#     if request.method == 'DELETE':
#         gym.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)

# class GymList(APIView):
#     def get(self, request):
#         gyms = Gym.objects.all()
#         serializer = GymSerializer(gyms, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = GymSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status= status.HTTP_201_CREATED
#                 )
#         return Response(
#             serializer.data,
#             status= status.HTTP_400_BAD_REQUEST
#             )

@api_view(['GET'])
def gym_search(request):

    if 'q' in request.GET:
        q = request.GET['q']
        multi = Q(Q(name__icontains=q) | Q(city__icontains=q) | Q(area__icontains=q))
        gym_search = Gym.objects.filter(multi)
    else:
        gym_search = Gym.objects.all()
    context = {'gyms': gym_search}
    return render(request, 'gym/search_results.html', context)

# def gym_searchform(request):
#     form = GymSearchForm(request.POST or None)

#     if request.method == 'POST':
#         queryset = Gym.objects.filter(name__icontaint=form['name'].value(),
#         city__icontaint=form['city'].value(),
#         area__icontaint=form['area'].value())