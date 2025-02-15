from django.urls import path
from .templateView.HomeView import *
from .templateView.NewsAndEventsView import *
from .templateView.UserLoginLogoutView import *
from .views import *

Api = [
    # login -- logout url
    path('login/', UserLogin, name='login'),
    path('logout/', UserLogout, name='logout'),
    
    path('api/v1/news-events/', NewsAndEventsView.as_view(), name='news-events'),
]

django_url = [
    path('', home, name='home'),

    # News And Events
    path('news-events/add/', addNewsEvents, name='addNewsEvents'),
    path('news-events/show/', showNewsEvents, name='showNewsEvents'),
    path('news-events/edit/<str:id>', editNewsEvents, name='editNewsEvents'),
    path('news-events/delete/<str:id>', deleteNewsEvents, name='deleteNewsEvents'),
]

urlpatterns = Api + django_url