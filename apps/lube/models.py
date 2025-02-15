from django.db import models
from core.models import BaseModel
from ckeditor.fields import RichTextField
from apps.brand.models import BrandModel

# Create your models here.
class QueryModel(BaseModel):
    """
    QueryModel for query
    """
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    brand = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=250, blank=True)
    quantity = models.IntegerField(blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class OurExpertsModel(BaseModel):
    """
    OurExpertsModel for about us
    """
    image = models.FileField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class AboutModel(BaseModel):
    """
    AboutModel for about us
    """
    hero_title = models.CharField(max_length=250, blank=True)
    hero_image = models.FileField(blank=True)
    image = models.FileField(blank=True)
    content = RichTextField(blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    director_name = models.CharField(max_length=50, blank=True)
    director_designation = models.CharField(max_length=100, blank=True)
    director_description = RichTextField(blank=True)
    director_image = models.FileField(blank=True)


class AboutSliderModel(BaseModel):
    """
    AboutSliderModel for about slider
    """
    title = models.CharField(max_length=300, blank=True)
    sub_title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class ContactDetailModel(BaseModel):
    """
    ContactDetailModel for contact details
    """
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.email


class GetInTouchModel(BaseModel):
    """
    GetInTouchModel for contact us
    """
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    cover_letter = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
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
    

class HomeModel(BaseModel):
    media = models.FileField(blank=True)
    hero_title = models.CharField(max_length=250, blank=True)
    find_title = models.CharField(max_length=300, blank=True)
    find_description = models.TextField(blank=True)
    find_media = models.FileField(blank=True)
    distribution_title = models.CharField(max_length=300, blank=True)
    distribution_description = models.TextField(blank=True)
    distribution_image = models.FileField(blank=True)

    def __str__(self):
        return self.id


class CompanyModel(BaseModel):
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(blank=True)
    video = models.FileField(blank=True)
    lubricant_distributions = models.IntegerField(blank=True, default=0)
    districts_covered = models.IntegerField(blank=True, default=0)
    types_of_products = models.IntegerField(blank=True , default=0)
    annual_production = models.IntegerField(blank=True, default=0)
    dealers_of_bangladesh = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title
    

class BusinessSolutionsModel(BaseModel):
    """
    BusinessSolutionsModel for Business and Solutions
    """
    brand = models.ForeignKey(BrandModel, related_name="business_solutions", on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(blank=True)
    title = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class AgricultureLubricantsModel(BaseModel):
    """
    AgricultureLubricantsModel for Agriculture lubricants
    """
    hero_image = models.FileField(null=True, blank=True)
    hero_title = models.CharField(max_length=250, blank=True)
    image = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    diagnostics_image = models.FileField(null=True, blank=True)
    diagnostics = models.TextField(blank=True)
    fluid_i_image = models.FileField(null=True, blank=True)
    fluid_i = models.TextField(blank=True)
    academy_image = models.FileField(null=True, blank=True)
    academy = models.TextField(blank=True)
    distribute_image = models.FileField(null=True, blank=True)
    distribute_title = models.CharField(max_length=250, blank=True)
    distribute_description = models.TextField(blank=True)

    def __str__(self):
        return self.hero_title
    

class AgricultureLubricantsSliderModel(BaseModel):
    """
    AgricultureLubricantsSliderModel for AgricultureLubricants slider
    """
    title = models.CharField(max_length=300, blank=True)
    sub_title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title
    

class DistributionDivisionModel(BaseModel):
    """
    DistributionDivisionModel for Distribution point
    """
    division = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.division

class DistributionDistrictModel(BaseModel):
    """
    DistributionDistrictModel for Distribution point
    """
    district = models.CharField(max_length=100, blank=True)
    division= models.ForeignKey(DistributionDivisionModel, related_name="distribution_district", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.district


class DistributionPointModel(BaseModel):
    """
    DistributionPointModel for Distribution point
    """
    district = models.ForeignKey(DistributionDistrictModel, related_name="distribution_point", on_delete=models.CASCADE, null=True, blank=True)
    dealer_name = models.CharField(max_length=100, null=True, blank=True)
    dealer_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.dealer_name


class DocumentModel(BaseModel):
    """
    DoumentModel for doucment
    """
    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        if self.id:
            return self.id
        else:
            return self.name
