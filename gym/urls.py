from django.urls import path, include

from . import views


urlpatterns = [
    # path('', views.gym_list, name='gym_list'),
    # path('<int:id>', views.gym_page, name='gym_page'),
    # path('api/fbvgymlist/', views.fbv_list),
    # path('api/fbvgympage/<int:id>', views.fbv_gym_page),
    # path('api/cbvgymlist/', views.GymList.as_view()),
    # path('api/cbvmixgymlist/', views.GymListMixins.as_view()),
    path('apis/', views.GymListGeneric.as_view()),
    path('apis/gym-<int:pk>', views.GymOperationGeneric.as_view()),
    
]
