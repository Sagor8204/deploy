from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import *
from apps.product.models import ProductModel
from apps.brand.models import BrandModel, BrandDetailsModel
from apps.lube.models import NewsAndEventsModel, BusinessSolutionsModel, OurExpertsModel, AboutSliderModel, AgricultureLubricantsSliderModel


@login_required(login_url="login")
def home(request):
    """
    Render the home page with counts of products, categories, and subcategories.
    """

    # Retrieve counts for products, categories, and subcategories
    counts = {
        "products": ProductModel.objects.count(),
        "brands": BrandModel.objects.count(),
        "brand_details": BrandDetailsModel.objects.count(),
        "news_events": NewsAndEventsModel.objects.count(),
        "business_solutions": BusinessSolutionsModel.objects.count(),
        "experts": OurExpertsModel.objects.count(),
        "about_slider": AboutSliderModel.objects.count(),
        "agriculture_lubricants_slider": AgricultureLubricantsSliderModel.objects.count(),
    }

    # Add 'active' for navigation highlighting
    counts['active'] = 'home'

    # Render the home template with the context
    return render(request, "home.html", counts)