from rest_framework import serializers
from .models import *


class BrandDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandDetailsModel
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['drand_details'] = BrandDetailsSerializer(BrandDetailsModel.objects.filter(brand=instance.id).last(),context={'request': self.context.get('request')}).data
        
        return representation
