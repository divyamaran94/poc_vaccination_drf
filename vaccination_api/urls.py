from django.urls import path, include
from rest_framework import routers
# from vaccination_api import views
from . import views
from django.contrib import admin

# admin.autodiscover()



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('vaccinecenters/', views.VaccinecenterList.as_view()),
    path('vaccinecenters/<int:pk>/', views.VaccinecenterDetail.as_view()),
    path('vaccinetypes/', views.VaccinetypeList.as_view()),
    path('vaccinetypes/<int:pk>/', views.VaccinetypeDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('appointments/', views.AppointmentList.as_view()),
    path('appointments/<int:pk>/', views.AppointmentList.as_view()),
    

    path('availabledate/', views.AvailabledateList.as_view()),
    # path('appointments/', views.Appointment_mixins.as_view()),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

# initializing the router
# router = routers.DefaultRouter()
# register each views or route
# router.register('vaccinecenters', views.VaccinecenterList)
# router.register('vaccinetypes', views.VaccinetypeList)
# router.register('appointments', views.AppointmentList)
# router.register('paradigms', views.ParadigmView)
# urlpatterns = [
#     path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
#     path('', include(router.urls)),
# ]


# router = routers.DefaultRouter()
# router.register(r'quotes', views.QuoteViewSet)
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]