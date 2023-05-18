from rest_framework import serializers
from .models import Vaccinecenter
from .models import Vaccinetype
from .models import User
from .models import Availabledate
from .models import Appointment
# from .models import Paradigm
# from .models import Quote



class VaccinecenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccinecenter
        fields = "__all__"
        # read_only_fields = ("created_by",)
    
    # def create(self, validated_data):
    #     if self.context["request"].user.is_authenticated:
    #         user = self.context["request"].user
    #         # user = self.request.user
    #         # validated_data['created_by'] = user
    #         #return Vac`cinecenter.objects.create(**validated_data, created_by=user)
    #     return Vaccinecenter.objects.create(**validated_data)


class VaccinetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccinetype
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AvailabledateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availabledate
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

# class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
#     # used to change the behaviour of a class or Model
#     class Meta:
#         # referencing the paradigm model
#         model = Paradigm
#         # listing the fields that will be displayed
#         fields = [
#             "id",
#             'url',
#             "name",
#         ]

# class QuoteSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Quote
#         fields = ('author', 'quote')