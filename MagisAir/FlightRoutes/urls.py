from django.urls import path

from. views import (LocationListView, FlightListView, RouteListView,)

urlpatterns = [
    path('locations', LocationListView.as_view(), name='location-table'),
    path('flights', FlightListView.as_view(), name='flight-table'),
    path('routes', RouteListView.as_view(), name='route-table'),
]

app_name='FlightRoutes'