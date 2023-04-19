from rest_framework import generics
from .models import Vaccinecenter
from .models import Vaccinetype

from .serializers import VaccinecenterSerializer
from .serializers import VaccinetypeSerializer
# from .permissions import IsVaccinecenterOwner
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin





class VaccinecenterList(generics.ListCreateAPIView):
    # permission_classes = [IsVaccinecenterOwner]
    queryset = Vaccinecenter.objects.all()
    serializer_class = VaccinecenterSerializer

class VaccinecenterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccinecenter.objects.all()
    serializer_class = VaccinecenterSerializer


# class VaccinetypeList(generics.ListCreateAPIView):
#     queryset = Vaccinetype.objects.all()
#     serializer_class = VaccinetypeSerializer
    
# class VaccinetypeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vaccinetype.objects.all()
#     serializer_class = VaccinetypeSerializer




# LIST and CREATE View Combine
class VaccinetypeList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Vaccinetype.objects.all()
    serializer_class=VaccinetypeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)    


# RETREIVE ,UPDATE and DELETE Combine 

class VaccinetypeDetail(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Vaccinetype.objects.all()
    serializer_class=VaccinetypeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # def put(self,request,*args,  **kwargs):
    #     return self.update(request, *args, **kwargs)  
    # def delete(self,request,*args,  **kwargs):
    #     return self.destroy(request, *args, **kwargs)