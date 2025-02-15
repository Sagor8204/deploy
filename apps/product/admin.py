from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(OilTypeModel)
admin.site.register(ProductRangeModel)
admin.site.register(ApplicationsModel)
admin.site.register(SectorsModel)
admin.site.register(ViscosityModel)
admin.site.register(LubricantCategoryModel)
admin.site.register(LubricantCategoryYearModel)
admin.site.register(LubricantEngineCapacityModel)
admin.site.register(LubricantSpecificationModel)