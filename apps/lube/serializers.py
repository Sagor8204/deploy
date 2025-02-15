from rest_framework import serializers
from .models import *

class NewsAndEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAndEventsModel
        fields = "__all__"