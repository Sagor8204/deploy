from rest_framework import status
from rest_framework.views import APIView
from core.response import CustomApiResponse as response
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.
class NewsAndEventsView(APIView):
    serializer_class = NewsAndEventsSerializer

    def get_queryset(self):
        return NewsAndEventsModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()
