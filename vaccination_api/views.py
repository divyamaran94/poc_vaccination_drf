from rest_framework import generics, permissions
from .models import Vaccinecenter
from .models import Vaccinetype
from .models import User
from .serializers import VaccinecenterSerializer
from .serializers import VaccinetypeSerializer
# from .permissions import IsVaccinecenterOwner
# from .permissions import AdminOrReadonly
from .permissions import IsOwnerOrReadOnly

from .serializers import UserSerializer
from .serializers import AvailabledateSerializer
from .serializers import AppointmentSerializer
from .permissions import IsAdminRole # IsObjectOwner IsAdminUserTest, 
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import viewsets,generics, serializers # permissions
from rest_framework.permissions import IsAuthenticated
from vaccination_api.models import *
from .serializers import * 
from django.contrib import admin
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.response import Response
from rest_framework import status

# admin.autodiscover()

# Create a mixin for list and create functionality
class VaccinecenterList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Vaccinecenter.objects.all()
    serializer_class = VaccinecenterSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)   

# Create a mixin for retrieve, update, and delete functionality
class VaccinecenterDetail(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Vaccinecenter.objects.all()
    serializer_class = VaccinecenterSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)  
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)



# LIST and CREATE View Combine
class VaccinetypeList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Vaccinetype.objects.all()
    serializer_class=VaccinetypeSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)   



# RETREIVE ,UPDATE and DELETE Combine 
class VaccinetypeDetail(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Vaccinetype.objects.all()
    serializer_class=VaccinetypeSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)  
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)


# LIST and CREATE View Combine
class UserList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)  


# RETREIVE ,UPDATE and DELETE Combine 
class UserDetail(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)  
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
        

class AvailabledateList(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset = Availabledate.objects.all()
    serializer_class=AvailabledateSerializer
    permission_classes = [IsAuthenticated, IsAdminRole]


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)   
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs) 




# LIST and CREATE View Combine
class AppointmentList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Appointment.objects.all()
    serializer_class=AppointmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)   

# RETREIVE ,UPDATE and DELETE Combine 
class AppointmentDetail(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Appointment.objects.all()
    serializer_class=AppointmentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)  
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)


# class Appointment_mixins(generics.GenericAPIView, 
#                                 ListModelMixin, 
#                                 CreateModelMixin,
#                                 RetrieveModelMixin,
#                                 UpdateModelMixin,
#                                 DestroyModelMixin):

# class AppointmentList(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin):
#     queryset = Appointment.objects.all()
#     serializer_class=AppointmentSerializer
#     permission_classes = [permissions.IsAuthenticated, IsObjectOwner]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self,request,*args,  **kwargs):
#         return self.create(request, *args, **kwargs)
#     def put(self,request,*args,  **kwargs):
#         return self.update(request, *args, **kwargs) 



#     serializer_class = AppointmentSerializer
#     queryset = Appointment.objects.all()

# class ParadigmView(viewsets.ModelViewSet):
#     queryset = Paradigm.objects.all()
#     # initializing the serializer
#     serializer_class = ParadigmSerializer
#     # it will automately overide the default permissions that is in settings.py
#     permission_classes = [permissions.IsAuthenticated]


# class VaccinetypeList(generics.ListCreateAPIView):
#     queryset = Vaccinetype.objects.all()
#     serializer_class = VaccinetypeSerializer
    
# class VaccinetypeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vaccinetype.objects.all()
#     serializer_class = VaccinetypeSerializer

 
# class QuoteViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
#     queryset = Quote.objects.all().order_by('id')
#     serializer_class = QuoteSerializer


# class VaccinecenterList(generics.ListCreateAPIView):
#     permission_classes = [IsVaccinecenterOwner]
#     # permission_classes = [AdminOrReadonly]
#     # permission_classes = [IsAdminUserTest]
#     # permission_classes = [permissions.IsAuthenticated]
#     # @login_required 

#     queryset = Vaccinecenter.objects.all()
#     serializer_class = VaccinecenterSerializer


# class VaccinecenterDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vaccinecenter.objects.all()
#     serializer_class = VaccinecenterSerializer


# permission_classes = [AdminOrReadonly]
# permission_classes = [IsAdminUserTest]
# permission_classes = [permissions.IsAuthenticated]



    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # permission_classes = [IsAdminUserTest]
    # permission_classes = (IsTier2OrAbove,)
    # permission_classes = [IsAdminUserTest]