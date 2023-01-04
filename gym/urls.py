from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.gym_list),
    path('<int:id>', views.gym_page),

]
