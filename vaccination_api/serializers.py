from rest_framework import serializers
from .models import Vaccinecenter
from .models import Vaccinetype



class VaccinecenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccinecenter
        fields = "__all__"
        read_only_fields = ("created_by",)
    
    def create(self, validated_data):
        if self.context["request"].user.is_authenticated:
            user = self.context["request"].user
            # user = self.request.user
            validated_data['created_by'] = user
            #return Vac`cinecenter.objects.create(**validated_data, created_by=user)
        return Vaccinecenter.objects.create(**validated_data)


class VaccinetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccinetype
        fields = "__all__"

