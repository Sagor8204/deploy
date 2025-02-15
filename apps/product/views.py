from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from core.response import CustomApiResponse as response
from .models import *
from .serializers import *
from django.db.models import Q


# Create your views here.
class ProductView(APIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        id = self.request.query_params.get('id')
        brand_id = self.request.query_params.get('brand_id')

        if id:
            try:
                data = self.queryset.get(id=id)
            except ProductModel.DoesNotExist:
                custom_response = response('error', 'Not Found', [], status.HTTP_404_NOT_FOUND)
                return custom_response.get_response()
            serializer = self.serializer_class(data, context={'request': request})
        else:
            data = self.queryset.filter(brand=brand_id)
            serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', "Successfully retrieved data.", serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()



class ProductFilterView(APIView):
   
    def get(self, request, *args, **kwargs):
        oil_type = OilTypeModel.objects.all()
        oil_type_serializer = OilTypeSerializer(oil_type,many=True)

        product_range = ProductRangeModel.objects.all()
        product_range_serializer = ProductRangeSerializer(product_range,many=True)

        viscosity = ViscosityModel.objects.all()
        viscosity_serializer = ViscositySerializer(viscosity,many=True)

        applications = ApplicationsModel.objects.all()
        applications_serializer = ApplicationsSerializer(applications,many=True)

        sectors = SectorsModel.objects.all()
        sectors_serializer = SectorsSerializer(sectors,many=True)

        data = {
            "oil_type":oil_type_serializer.data,
            "product_range":product_range_serializer.data,
            "viscosity":viscosity_serializer.data,
            "applications":applications_serializer.data,
            "sectors":sectors_serializer.data,
        }
        custom_response = response('success', "Successfully retrieved data.", data, status.HTTP_200_OK)
        return custom_response.get_response()
    

class LubricantView(APIView):
    queryset = LubricantCategoryModel.objects.all()
    serializer_class = LubricantCategorySerializer

    def get_queryset(self):
        return LubricantCategoryModel.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()


class ProductFilterAPIView(APIView):
    """
    API to filter products based on oil_type, product_range, viscosity, applications, and sectors
    """

    def get(self, request, *args, **kwars):
        # Get filter parameters form query params
        brand = request.query_params.get('brand')
        oil_type = request.query_params.get('oil_type')
        product_range = request.query_params.get('product_range')
        viscosity = request.query_params.get('viscosity')
        applications = request.query_params.get('applications')
        sectors = request.query_params.get('sectors')

        # If brand is not provided, raise and error
        if not brand:
            raise ValidationError({'brand': 'This field is required.'})

        # Filter products dynamically based on provided query params
        products = ProductModel.objects.filter(brand=brand)

        if oil_type:
            oil_type_list = oil_type.split(",")
            products = products.filter(oil_type__in=oil_type_list)
        if product_range:
            product_range_list = product_range.split(",")
            products = products.filter(product_range__in=product_range_list)
        if viscosity:
            viscosity_list = viscosity.split(",")
            products = products.filter(viscosity__in=viscosity_list)
        if applications:
            application_list = applications.split(",")
            products = products.filter(applications__in=application_list)
        if sectors:
            sectors_list = sectors.split(",")
            products = products.filter(sectors__in=sectors_list)

        serializer = ProductSerializer(products, many=True)

        custom_response = response("success", 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()