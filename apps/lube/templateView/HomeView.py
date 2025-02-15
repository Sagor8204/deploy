from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import *
from apps.lube.models import NewsAndEventsModel


@login_required(login_url="login")
def home(request):
    """
    Render the home page with counts of products, categories, and subcategories.
    """

    # Retrieve counts for products, categories, and subcategories
    counts = {
        "news_events": NewsAndEventsModel.objects.count(),
    }

    # Add 'active' for navigation highlighting
    counts['active'] = 'home'

    # Render the home template with the context
    return render(request, "home.html", counts)