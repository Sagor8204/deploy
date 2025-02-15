from rest_framework import serializers
from .models import *

class HomeContentSerializer(serializers.ModelSerializer):
    company_title = serializers.SerializerMethodField()
    company_description = serializers.SerializerMethodField()
    company_image = serializers.SerializerMethodField()
    company_video = serializers.SerializerMethodField()
    lubricant_distributions = serializers.SerializerMethodField()
    districts_covered = serializers.SerializerMethodField()
    types_of_products = serializers.SerializerMethodField()

    class Meta:
        model = HomeModel
        fields = "__all__"

    def get_company_title(self, obj):
        data = CompanyModel.objects.first()
        return data.title if data else None
    
    def get_company_description(self, obj):
        data = CompanyModel.objects.first()
        return data.description if data else None

    def get_company_image(self, obj):
        request = self.context.get('request')
        data = CompanyModel.objects.first()
        if data and data.image:
            return request.build_absolute_uri(data.image.url) if request else data.image.url
        return None
    
    def get_company_video(self, obj):
        request = self.context.get('request')
        data = CompanyModel.objects.first()
        if data and data.video:
            return request.build_absolute_uri(data.video.url) if request else data.video.url
        return None
    
    def get_lubricant_distributions(self, obj):
        data = CompanyModel.objects.first()
        return data.lubricant_distributions if data else None
    
    def get_districts_covered(self, obj):
        data = CompanyModel.objects.first()
        return data.districts_covered if data else None
    
    def get_types_of_products(self, obj):
        data = CompanyModel.objects.first()
        return data.types_of_products if data else None

class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetailModel
        fields = "__all__"

    
class GetInTouchSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    cover_letter = serializers.CharField(required=True)

    class Meta:
        model = GetInTouchModel
        fields = "__all__"

    
class OurExpertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurExpertsModel
        fields = "__all__"


class AboutSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSliderModel
        fields = "__all__"



class AboutSerializer(serializers.ModelSerializer):
    our_experts = serializers.SerializerMethodField()
    sliders = serializers.SerializerMethodField()
    annual_production = serializers.SerializerMethodField()
    districts_covered = serializers.SerializerMethodField()
    dealers_of_bangladesh = serializers.SerializerMethodField()

    class Meta:
        model = AboutModel
        fields = "__all__"

    def get_our_experts(self, obj):
        experts = OurExpertsModel.objects.all()
        return OurExpertsSerializer(experts, many=True, context=self.context).data
    
    def get_sliders(self, obj):
        datas = AboutSliderModel.objects.all()
        return AboutSliderSerializer(datas, many=True, context=self.context).data
    
    def get_annual_production(self, obj):
        data = CompanyModel.objects.first()
        return data.annual_production if data else None
    
    def get_districts_covered(self, obj):
        data = CompanyModel.objects.first()
        return data.districts_covered if data else None
    
    def get_dealers_of_bangladesh(self, obj):
        data = CompanyModel.objects.first()
        return data.dealers_of_bangladesh if data else None
    

    
class QuerySerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    brand = serializers.CharField(required=True)
    product = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = QueryModel
        fields = "__all__"



class NewsAndEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAndEventsModel
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandModel
        fields = "__all__"


class BusinessSolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSolutionsModel
        fields = "__all__"

    def to_representation(self, instance):

        data = super().to_representation(instance)  
        data["brand"] = BrandSerializer(instance.brand,context={'request': self.context.get('request')}).data

        return data


class AgricultureLubricantsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureLubricantsSliderModel
        fields = "__all__"


class AgricultureLubricantsSerializer(serializers.ModelSerializer):
    sliders = serializers.SerializerMethodField()

    class Meta:
        model = AgricultureLubricantsModel
        fields = "__all__"

    def get_sliders(self,obj):
        datas = AgricultureLubricantsSliderModel.objects.all()
        return AgricultureLubricantsSliderSerializer(datas, many=True, context=self.context).data


class DistributionPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionPointModel
        fields = "__all__"


class DistributionDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionDistrictModel
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['dealers_point'] = DistributionPointSerializer(instance.distribution_point.all(), many=True).data
        
        return representation


class DistributionDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionDivisionModel
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['districts'] = DistributionDistrictSerializer(instance.distribution_district.all(), many=True).data

        return representation


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = "__all__"
