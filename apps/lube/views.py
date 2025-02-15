from rest_framework import status
from rest_framework.views import APIView
from core.response import CustomApiResponse as response
from .models import *
from .serializers import *
from django.db.models import Q

# Create your views here.
class ContactDetailView(APIView):
    serializer_class = ContactDetailSerializer

    def get_queryset(self):
        return ContactDetailModel.objects.all()

    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True)

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()
    
class GetInTouchView(APIView):
    serializer_class = GetInTouchSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            custom_response = response('success', 'Data successfully saved.', serializer.data, status.HTTP_201_CREATED)
            return custom_response.get_response()
        else:
            custom_response = response('error', 'Validation failed.', serializer.errors, status.HTTP_400_BAD_REQUEST)
            return custom_response.get_response()

class AboutView(APIView):
    serializer_class = AboutSerializer

    def get_queryset(self):
        return AboutModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()


class QueryView(APIView):
    serializer_class = QuerySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            custom_response = response('success', 'Data successfully saved.', serializer.data, status.HTTP_201_CREATED)
            return custom_response.get_response()
        else:
            custom_response = response('error', 'Validation failed.', serializer.errors, status.HTTP_400_BAD_REQUEST)
            return custom_response.get_response()
        


class NewsAndEventsView(APIView):
    serializer_class = NewsAndEventsSerializer

    def get_queryset(self):
        return NewsAndEventsModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()


class BusinessSolutionsView(APIView):
    serializer_class = BusinessSolutionsSerializer

    def get_queryset(self):
        return BusinessSolutionsModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()



class HomeContentView(APIView):
    serializer_class = HomeContentSerializer

    def get_queryset(self):
        return HomeModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()



class AgricultureLubricantsView(APIView):
    serializer_class = AgricultureLubricantsSerializer

    def get_queryset(self):
        return AgricultureLubricantsModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()


class DistributionView(APIView):
    serializer_class = DistributionDivisionSerializer

    def get_queryset(self):
        return DistributionDivisionModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()

class DocumentView(APIView):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return DocumentModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many=True, context={'request': request})

        custom_response = response('success', 'Successfully retrieved data.', serializer.data, status.HTTP_200_OK)
        return custom_response.get_response()

