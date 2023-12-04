from django.contrib import admin
from .models import Flight, Location, Route

class FlightAdmin(admin.ModelAdmin):
    model = Flight
    search_fields = ('flight_id',)
    list_display = ('flight_id', 'flt_route',
                    'flt_datetime_departure',
                    'flt_datetime_arrival',)

class LocationAdmin(admin.ModelAdmin):
    model = Location
    search_fields = ('location_id',)
    list_display = ('location_id', 'loc_name',)

class RouteAdmin(admin.ModelAdmin):
    model = Route
    search_fields = ('route_id',)
    list_display = ('route_id', 'rt_origin', 
                    'rt_destination', 'rt_price',)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Route, RouteAdmin)