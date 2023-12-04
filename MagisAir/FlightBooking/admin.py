from django.contrib import admin
from .models import Booking, BookingAdditionalitem, Passenger, Additionalitem, Flight
# Register your models here.

class PassengerAdmin(admin.ModelAdmin):
    model = Passenger
    search_fields = ('passenger_id',)
    list_display = ('passenger_id', 'pax_lname',
                    'pax_fname',
                    'pax_birthdate',)

class FlightAdmin(admin.ModelAdmin):
    model = Flight
    search_fields = ('flight_id',)
    list_display = ('flight_id', 'flt_route',
                    'flt_datetime_departure',
                    'flt_datetime_arrival',)

class BookingAdmin(admin.ModelAdmin):
    model = Booking
    search_fields = ('bkg_passenger', 'bkg_flight',)
    list_display = ('bkg_passenger', 'bkg_flight',)

class AdditionalitemAdmin(admin.ModelAdmin):
    model = Additionalitem
    search_fields = ('additionalitem_id',)
    list_display = ('additionalitem_id', 'aitm_item', 
                    'aitm_itemdesc', 'aitm_cost',)

class BookingAdditionalitemAdmin(admin.ModelAdmin):
    model = BookingAdditionalitem
    search_fields = ('bai_passenger', 'bai_flight',
                    'bai_additionalitem')
    list_display = ('bai_passenger', 'bai_flight',
                    'bai_additionalitem', 'bai_quantity')

admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Additionalitem, AdditionalitemAdmin)
admin.site.register(BookingAdditionalitem, BookingAdditionalitemAdmin)
admin.site.register(Flight, FlightAdmin)