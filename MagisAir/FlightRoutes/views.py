from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Flight, Location, Route

def SQL_Query1(request):
    flights = Flight.objects.raw("SELECT flight.flight_id, origin.loc_name Origin, destination.loc_name Destination, flight.flt_datetime_departure AS Departure, flight.flt_datetime_arrival AS Arrival, CONCAT(HOUR(TIMEDIFF(flight.flt_datetime_arrival, flight.flt_datetime_departure)), ' hours ', MINUTE(TIMEDIFF(flight.flt_datetime_arrival, flight.flt_datetime_departure)), ' minutes') Duration FROM flight, route, location origin, location destination WHERE flight.flt_route_id = route.route_id AND route.rt_origin = origin.location_id AND route.rt_destination = destination.location_id;")
    print(flights)
    return render(request, 'FlightRoutes/SQL_Query1.html', {'data': flights})

class LocationListView(ListView):
    model = Location
    def get(self, request):
        locations = Location.objects.all()
        return render(request, 'FlightRoutes/locations.html', {
            'locations': locations
        })

class FlightListView(ListView):
    model = Flight
    def get(self, request):
        flights = Flight.objects.all()
        return render(request, 'FlightRoutes/flights.html', {
            'flights': flights
        })

class RouteListView(ListView):
    model = Route
    def get(self, request):
        routes = Route.objects.all()
        return render(request, 'FlightRoutes/routes.html', {
            'routes': routes
        })

class LocationCreateView(CreateView):
    model = Location
    fields = '__all__'
    template_name = 'FlightRoutes/locationsCreate.html'

class FlightCreateView(CreateView):
    model = Flight
    fields = '__all__'
    template_name = 'FlightRoutes/flightsCreate.html'

class RouteCreateView(CreateView):
    model = Route
    fields = '__all__'
    template_name = 'FlightRoutes/routesCreate.html'

class LocationDetailview(DetailView):
    model = Location
    template_name = 'FlightRoutes/successfullyAdded.html'

class FlightDetailView(DetailView):
    model = Flight
    template_name = 'FlightRoutes/successfullyAdded.html'

class RouteDetailView(DetailView):
    model = Route
    template_name = 'FlightRoutes/successfullyAdded.html'