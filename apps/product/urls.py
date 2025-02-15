from django.urls import path
from .views import *
from .templateViews.ProductTemView import *
from .templateViews.OilTypeView import *
from .templateViews.ProductRangeView import *
from .templateViews.ViscosityView import *
from .templateViews.ApplicationsView import *
from .templateViews.SectorsView import *
from .templateViews.LubricantCategoryView import *
from .templateViews.LubricantCategoryYearView import *
from .templateViews.LubricantEngineCapacityView import *
from .templateViews.LubricantSpecificationView import *

Api = [
    path('api/v1/products/', ProductView.as_view(), name='products'),
    path('api/v1/filters/', ProductFilterView.as_view(), name='product_filter'),
    path('api/v1/lubricants/', LubricantView.as_view(), name='lubricants'),
    path('api/v1/products/filter/', ProductFilterAPIView.as_view(), name='product-filter'),
]

django_url = [
    # Product
    path('product/add/', addProduct, name='addProduct'),
    path('product/show/', showProduct, name='showProduct'),
    path('product/edit/<str:id>', editProduct, name='editProduct'),
    path('product/delete/<str:id>', deleteProduct, name='deleteProduct'),

    # Oil Type
    path('product-oil-type/add/', addOilType, name='addOilType'),
    path('product-oil-type/show/', showOilType, name='showOilType'),
    path('product-oil-type/edit/<str:id>', editOilType, name='editOilType'),
    path('product-oil-type/delete/<str:id>', deleteOilType, name='deleteOilType'),

    # Product Range
    path('product-range/add/', addProductRange, name='addProductRange'),
    path('product-range/show/', showProductRange, name='showProductRange'),
    path('product-range/edit/<str:id>', editProductRange, name='editProductRange'),
    path('product-range/delete/<str:id>', deleteProductRange, name='deleteProductRange'),

    # Viscosity
    path('product-viscosity/add/', addViscosity, name='addViscosity'),
    path('product-viscosity/show/', showViscosity, name='showViscosity'),
    path('product-viscosity/edit/<str:id>', editViscosity, name='editViscosity'),
    path('product-viscosity/delete/<str:id>', deleteViscosity, name='deleteViscosity'),

    # Applications
    path('product-applications/add/', addApplications, name='addApplications'),
    path('product-applications/show/', showApplications, name='showApplications'),
    path('product-applications/edit/<str:id>', editApplications, name='editApplications'),
    path('product-applications/delete/<str:id>', deleteApplications, name='deleteApplications'),

    # Sectors
    path('product-sectors/add/', addSectors, name='addSectors'),
    path('product-sectors/show/', showSectors, name='showSectors'),
    path('product-sectors/edit/<str:id>', editSectors, name='editSectors'),
    path('product-sectors/delete/<str:id>', deleteSectors, name='deleteSectors'),

    # Lubricant Category
    path('category/add/', addLubricantCategory, name='addLubricantCategory'),
    path('category/show/', showLubricantCategory, name='showLubricantCategory'),
    path('category/edit/<str:id>', editLubricantCategory, name='editLubricantCategory'),
    path('category/delete/<str:id>', deleteLubricantCategory, name='deleteLubricantCategory'),

    # Lubricant year
    path('year/add/', addLubricantYear, name='addLubricantYear'),
    path('year/show/', showLubricantYear, name='showLubricantYear'),
    path('year/edit/<str:id>', editLubricantYear, name='editLubricantYear'),
    path('year/delete/<str:id>', deleteLubricantYear, name='deleteLubricantYear'),

    # Lubricant Engine Capacity
    path('engine-capacity/add/', addLubricantEngineCapacity, name='addLubricantEngineCapacity'),
    path('engine-capacity/show/', showLubricantEngineCapacity, name='showLubricantEngineCapacity'),
    path('engine-capacity/edit/<str:id>', editLubricantEngineCapacity, name='editLubricantEngineCapacity'),
    path('engine-capacity/delete/<str:id>', deleteLubricantEngineCapacity, name='deleteLubricantEngineCapacity'),

    # Lubricant Specification
    path('specification/add/', addLubricantSpecification, name='addLubricantSpecification'),
    path('specification/show/', showLubricantSpecification, name='showLubricantSpecification'),
    path('specification/edit/<str:id>', editLubricantSpecification, name='editLubricantSpecification'),
    path('specification/delete/<str:id>', deleteLubricantSpecification, name='deleteLubricantSpecification'),
]

urlpatterns = Api + django_url