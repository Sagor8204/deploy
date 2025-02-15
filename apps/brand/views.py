from rest_framework import status
from rest_framework.views import APIView
from core.response import CustomApiResponse as response
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.
class BrandView(APIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        return BrandModel.objects.all().order_by('order')
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', "Successfully retrieved data.", serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()


class BrandDetailsView(APIView):
    queryset = BrandDetailsModel.objects.all()
    serializer_class = BrandDetailsSerializer
    
    def get(self, request, *args, **kwargs):
        brand_id = self.request.query_params.get('brand_id')
        
        if id:
            try:
                data = self.queryset.get(brand=brand_id)
            except BrandDetailsModel.DoesNotExist:
                custom_response = response('error', 'Not Found', [], status.HTTP_404_NOT_FOUND)
                return custom_response.get_response()
            
            serializer = self.serializer_class(data, context={'request': request})
        
        else:
            data = BrandDetailsModel.objects.all()
            serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', "Successfully retrieved data.", serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()
