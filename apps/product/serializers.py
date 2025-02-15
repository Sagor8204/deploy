from rest_framework import serializers
from .models import *



class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandModel
        fields = "__all__"

class OilTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OilTypeModel
        exclude = ["created_at","updated_at","is_active"]


class ProductRangeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductRangeModel
        exclude = ["created_at","updated_at","is_active"]

class ViscositySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ViscosityModel
        exclude = ["created_at","updated_at","is_active"]

class ApplicationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ApplicationsModel
        exclude = ["created_at","updated_at","is_active"]

class SectorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SectorsModel
        exclude = ["created_at","updated_at","is_active"]




class ProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductModel
        fields = "__all__"

    def to_representation(self, instance):

        data = super().to_representation(instance)  
        data["brand"] = BrandSerializer(instance.brand,context={'request': self.context.get('request')}).data
        data["viscosity"] = ViscositySerializer(instance.viscosity).data
        data["applications"] = ApplicationsSerializer(instance.applications).data
        # data["oil_type"] = OilTypeSerializer(instance.oil_type).data
        data["product_range"] = ProductRangeSerializer(instance.product_range).data
        data["sectors"] = SectorsSerializer(instance.sectors).data

        return data


class LubricantSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LubricantSpecificationModel
        fields = "__all__"

class LubricantEngineCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LubricantEngineCapacityModel
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['specifications'] = LubricantSpecificationSerializer(instance.Lubricant_specification.all(), many=True).data

        return data


class LubricantCategoryYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = LubricantCategoryYearModel
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['engine_capacity'] = LubricantEngineCapacitySerializer(instance.Lubricant_engine_capacity.all(), many=True).data

        return data


class LubricantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LubricantCategoryModel
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['years'] = LubricantCategoryYearSerializer(instance.lubricant_year.all(), many=True).data

        return data
