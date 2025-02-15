from django.db import models
from core.models import BaseModel
from apps.brand.models import BrandModel

# Create your models here.
class OilTypeModel(BaseModel):
    """
    OilTypeModel for product filter by oil type
    """
    title = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class ProductRangeModel(BaseModel):
    """
    ProductRangeModel for product filter by oil type
    """
    title = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class ViscosityModel(BaseModel):
    """
    ViscosityModel for product filter by oil type
    """
    title = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class ApplicationsModel(BaseModel):
    """
    ApplicationsModel for product filter by oil type
    """
    title = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class SectorsModel(BaseModel):
    """
    SectorsModel for product filter by oil type
    """
    title = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class ProductModel(BaseModel):
    """
    Product Model for products
    """
    brand = models.ForeignKey(BrandModel, related_name="product", on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=300, blank=True)
    image = models.FileField(blank=True)
    name = models.CharField(max_length=300, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    viscosity = models.ForeignKey(ViscosityModel, related_name="product", on_delete=models.CASCADE, null=True, blank=True)
    industry_specifications = models.CharField(max_length=300, null=True, blank=True)
    applications = models.ForeignKey(ApplicationsModel, related_name="product", on_delete=models.CASCADE, null=True, blank=True)
    oil_type = models.ForeignKey(OilTypeModel, related_name="product", on_delete=models.CASCADE, null=True, blank=True)
    product_range = models.ForeignKey(ProductRangeModel, related_name="product", on_delete=models.CASCADE, null=True, blank=True)
    FG_code = models.IntegerField(default=0, null=True, blank=True)
    OEM_approvals = models.CharField(max_length=300, null=True, blank=True)
    OEM_performance = models.CharField(max_length=300, null=True, blank=True)
    sectors = models.ForeignKey(SectorsModel, related_name="product", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.brand:
            self.brand_name = self.brand.name
        super().save(*args, **kwargs)


class LubricantCategoryModel(BaseModel):
    """
    LubricantCategoryModel for lubircant Category name
    """
    category = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.category


class LubricantCategoryYearModel(BaseModel):
    """
    LubricantCategoryYearModel for lubircant CategoryYear name
    """
    category = models.ForeignKey(LubricantCategoryModel, related_name="lubricant_year", on_delete=models.CASCADE)
    year = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.year}"



class LubricantEngineCapacityModel(BaseModel):
    """
    LubricantEngineCapacityModel for lubircant EngineCapacity name
    """
    year = models.ForeignKey(LubricantCategoryYearModel, related_name="Lubricant_engine_capacity", on_delete=models.CASCADE)
    engine_capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.engine_capacity)


class LubricantSpecificationModel(BaseModel):
    """
    LubricantSpecificationModel for lubircant Specification name
    """
    engine_capacity = models.ForeignKey(LubricantEngineCapacityModel, related_name="Lubricant_specification", on_delete=models.CASCADE)
    model_name = models.CharField(max_length=250, null=True, blank=True)
    fuel_type = models.CharField(max_length=250, null=True, blank=True)
    power = models.CharField(max_length=250, null=True, blank=True)
    production_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.model_name
