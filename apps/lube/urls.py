from django.urls import path
from .templateView.HomeView import *
from .templateView.OurExpertsview import *
from .templateView.singleView import *
from .templateView.NewsAndEventsView import *
from .templateView.AboutSliderView import *
from .templateView.BusinessSolutionsView import *
from .templateView.AgricultureLubricantsSliderView import *
from .templateView.DistributionDivisionView import *
from .templateView.DistributionDistrictView import *
from .templateView.DistributionPontView import *
from .templateView.DocumentView import *
from .templateView.UserLoginLogoutView import *
from .views import *

Api = [
    # login -- logout url
    path('login/', UserLogin, name='login'),
    path('logout/', UserLogout, name='logout'),
    
    path('api/v1/contact-detail/', ContactDetailView.as_view(), name='contact-detail'),
    path('api/v1/getin-touch/', GetInTouchView.as_view(), name='getin-touch'),
    path('api/v1/about/', AboutView.as_view(), name='about'),
    path('api/v1/query/', QueryView.as_view(), name='query'),
    path('api/v1/news-events/', NewsAndEventsView.as_view(), name='news-events'),
    path('api/v1/home/', HomeContentView.as_view(), name='home'),
    path('api/v1/business-solutions/', BusinessSolutionsView.as_view(), name='business-solutions'),
    path('api/v1/agriculture-ubricants/', AgricultureLubricantsView.as_view(), name='agriculture-ubricants'),
    path('api/v1/distribution-point/', DistributionView.as_view(), name='distribution-point'),
    path('api/v1/documents/', DocumentView.as_view(), name='documents'),
]

django_url = [
    path('', home, name='home'),

    # Our Expert
    path('our-experts/add/', addOurExperts, name='addOurExperts'),
    path('our-experts/show/', showOurExperts, name='showOurExperts'),
    path('our-experts/edit/<str:id>', editOurExperts, name='editOurExperts'),
    path('our-experts/delete/<str:id>', deleteOurExperts, name='deleteOurExperts'),

    # Home content
    path('home-content/', homeContentData, name='homeContentData'),
    
    # Home content
    path('company-details/', companyDetailsData, name='companyDetailsData'),

    # About Us
    path('about-us/', aboutData, name='aboutData'),

    # Agriculture Lubricants
    path('agriculture-lubricants/', agricultureLubricantsData, name='agricultureLubricantsData'),

    # Contact Details
    path('contact-details/', contactDetails, name='contactDetails'),
    path('about-us/', aboutData, name='aboutData'),

    # Getintouch
    path('getintouch/', showGetInTouch, name='showGetInTouch'),
    path('mark-read<str:id>/', markRead, name='markRead'),
    path('about-us/', aboutData, name='aboutData'),

    # Query
    path('query/', showQuery, name='showQuery'),
    path('mark-read/query/<str:id>/', markReadQuery, name='markReadQuery'),

    # News And Events
    path('news-events/add/', addNewsEvents, name='addNewsEvents'),
    path('news-events/show/', showNewsEvents, name='showNewsEvents'),
    path('news-events/edit/<str:id>', editNewsEvents, name='editNewsEvents'),
    path('news-events/delete/<str:id>', deleteNewsEvents, name='deleteNewsEvents'),

    # News And Events
    path('about-slider/add/', addAboutSlider, name='addAboutSlider'),
    path('about-slider/show/', showAboutSlider, name='showAboutSlider'),
    path('about-slider/edit/<str:id>', editAboutSlider, name='editAboutSlider'),
    path('about-slider/delete/<str:id>', deleteAboutSlider, name='deleteAboutSlider'),

    # Business Solutions
    path('business-solutions/add/', addBusinessSolutions, name='addBusinessSolutions'),
    path('business-solutions/show/', showBusinessSolutions, name='showBusinessSolutions'),
    path('business-solutions/edit/<str:id>', editBusinessSolutions, name='editBusinessSolutions'),
    path('business-solutions/delete/<str:id>', deleteBusinessSolutions, name='deleteBusinessSolutions'),

    # Agriculture Lubricants
    path('agriculture-lubricants-slider/add/', addAgricultureLubricantsSlider, name='addAgricultureLubricantsSlider'),
    path('agriculture-lubricants-slider/show/', showAgricultureLubricantsSlider, name='showAgricultureLubricantsSlider'),
    path('agriculture-lubricants-slider/edit/<str:id>', editAgricultureLubricantsSlider, name='editAgricultureLubricantsSlider'),
    path('agriculture-lubricants-slider/delete/<str:id>', deleteAgricultureLubricantsSlider, name='deleteAgricultureLubricantsSlider'),

    # Division
    path('division/add/', addDivision, name='addDivision'),
    path('division/show/', showDivision, name='showDivision'),
    path('division/edit/<str:id>', editDivision, name='editDivision'),
    path('division/delete/<str:id>', deleteDivision, name='deleteDivision'),

    # District
    path('district/add/', addDistrict, name='addDistrict'),
    path('district/show/', showDistrict, name='showDistrict'),
    path('district/edit/<str:id>', editDistrict, name='editDistrict'),
    path('district/delete/<str:id>', deleteDistrict, name='deleteDistrict'),

    # DistributionPoint
    path('distribution-point/add/', addDistributionPoint, name='addDistributionPoint'),
    path('distribution-point/show/', showDistributionPoint, name='showDistributionPoint'),
    path('distribution-point/edit/<str:id>', editDistributionPoint, name='editDistributionPoint'),
    path('distribution-point/delete/<str:id>', deleteDistributionPoint, name='deleteDistributionPoint'),

    # Document View
    path('document/add/', addDocument, name='addDocument'),
    path('document/show/', showDocument, name='showDocument'),
    path('document/edit/<str:id>', editDocument, name='editDocument'),
    path('document/delete/<str:id>', deleteDocument, name='deleteDocument'),
]

urlpatterns = Api + django_url