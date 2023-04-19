from django.urls import path
from vaccination_api import views
urlpatterns = [
    path('vaccinecenters/', views.VaccinecenterList.as_view()),
    path('vaccinecenters/<int:pk>/', views.VaccinecenterDetail.as_view()),
    path('vaccinetypes/', views.VaccinetypeList.as_view()),
    path('vaccinetypes/<int:pk>/', views.VaccinetypeDetail.as_view()),
    ]
