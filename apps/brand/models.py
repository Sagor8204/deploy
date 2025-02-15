from ckeditor.fields import RichTextField
from django.db import models
from core.models import BaseModel


# Create your models here.
class BrandModel(BaseModel):
    """
    BrandModel for Brand
    """
    name = models.CharField(max_length=300, blank=True)
    image = models.FileField(blank=True)
    order = models.IntegerField(default=0, null=True ,blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
    

class BrandDetailsModel(BaseModel):
    """
    BrandDetailsModel for each brand details
    """
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.FileField(null=True, blank=True)
    hero_media = models.FileField(blank=True)
    brand = models.ForeignKey(BrandModel, related_name="brand_details", on_delete=models.CASCADE)
    efficiency_title = models.CharField(max_length=500, blank=True)
    efficiency_description = models.TextField(blank=True)
    efficiency_image = models.FileField(blank=True)
    why_right_choice_title = models.CharField(max_length=500, blank=True)
    why_right_choice_description = models.TextField(blank=True)
    what_makes_different = models.TextField(blank=True)
    what_makes_different_image = models.FileField(blank=True)
    left_content = RichTextField(blank=True)
    right_content = RichTextField(blank=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.id
