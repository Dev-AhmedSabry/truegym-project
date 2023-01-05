from django.urls import path

from . import views


urlpatterns = [
    path('api/', views.PartnerListGeneric.as_view()),
    path('api/partner_<int:pk>', views.PartnerOperationGeneric.as_view()),
]