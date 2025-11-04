
from django.contrib import admin
from django.urls import path
from home.views import index,about,services,regional_reach,contact, quote_request_view, service_detail_view ,logistics,ShipBroking,VesselAgency
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('about', about,name="about"),
    path('services', services,name="services"),
    path('regional_reach', regional_reach,name="regional_reach"),
    path('contact', contact,name="contact"),
    path('quote_request', quote_request_view, name='quote_request'),
    path('mock_api/logistics', logistics),
    path('mock_api/broking', ShipBroking),
    path('VesselAgency', VesselAgency),
    path('logistics', logistics),
    path('logistics', logistics),
    
    # URL for handling the HTMX GET requests for the service tabs
    # This expects a slug (e.g., 'port-agency', 'logistics') to be passed to the view
    path('services/<str:service_id>', service_detail_view, name='service_details'),
    path('', index),
]
