from django.db import models
from core.models import BaseModel

# Create your models here.
class NewsAndEventsModel(BaseModel):
    """
    NewsAndEventsModel for NewsAndEvents
    """
    image = models.FileField(blank=True)
    date = models.DateField(blank=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    