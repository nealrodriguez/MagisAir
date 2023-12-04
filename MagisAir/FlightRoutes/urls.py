from django.urls import path

from. views import (LocationListView, FlightListView, RouteListView,
                    LocationCreateView, FlightCreateView, RouteCreateView,
                    LocationDetailview, FlightDetailView, RouteDetailView,
                    SQL_Query1)

urlpatterns = [
    path('locations', LocationListView.as_view(), name='location-table'),
    path('flights', FlightListView.as_view(), name='flight-table'),
    path('routes', RouteListView.as_view(), name='route-table'),
    path('locations/add', LocationCreateView.as_view(), name='location-add'),
    path('flights/add', FlightCreateView.as_view(), name='flight-add'),
    path('routes/add', RouteCreateView.as_view(), name='route-add'),
    path('locations/<pk>_added', LocationDetailview.as_view(), name='added-location'),
    path('flights/<pk>_added', FlightDetailView.as_view(), name='added-flight'),
    path('routes/<pk>_added', RouteDetailView.as_view(), name='added-route'),
    path('SQL_Query1', SQL_Query1, name='SQL_Query1')
]

app_name='FlightRoutes'