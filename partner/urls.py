from django.urls import path

from . import views


urlpatterns = [
    path('apis/', views.PartnerListGeneric.as_view()),
    path('apis/partner-<int:pk>', views.PartnerOperationGeneric.as_view()),
]