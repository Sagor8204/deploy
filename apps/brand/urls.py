from django.urls import path
from .templateViews.BrandView import *
from .templateViews.BrandDetailsView import *
from .views import *

Api = [
    path('api/v1/brand/', BrandView.as_view(), name="brand"),
    path('api/v1/brand-details/', BrandDetailsView.as_view(), name="brand-details"),
]

django_url = [
    # Brand
    path('brand/add/', addBrand, name='addBrand'),
    path('brand/show/', showBrand, name='showBrand'),
    path('brand/edit/<str:id>', editBrand, name='editBrand'),
    path('brand/delete/<str:id>', deleteBrand, name='deleteBrand'),

    # Brand Details
    path('brand-details/add/', addBrandDetails, name='addBrandDetails'),
    path('brand-details/show/', showBrandDetails, name='showBrandDetails'),
    path('brand-details/edit/<str:id>', editBrandDetails, name='editBrandDetails'),
    path('brand-details/delete/<str:id>', deleteBrandDetails, name='deleteBrandDetails'),
]

urlpatterns = Api + django_url