from django import forms
from .models import Location, Flight, Route

class LocationForm(forms.ModelForm):
    class meta:
        model = Location
        fields = ['location_id',
                'loc_name' ]

class FlightForm(forms.ModelForm):
    class meta:
        model = Flight
        fields = ['flight_id', 'flt_route',
                'flt_datetime_departure', 'flt_datetime_arrival']

class RouteForm (forms.ModelForm):
    class meta:
        model = Route
        fields = ['route_id', 'rt_origin',
                'rt_destination', 'rt_price']