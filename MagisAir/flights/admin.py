from django.contrib import admin

# Register your models here.
from .models import Additionalitem, Booking, BookingAdditionalitem, CrewAssignment, Flight, Location, Passenger, Route

class AdditionalitemAdmin(admin.ModelAdmin):
    model = Additionalitem

    search_fields = ('additionalitem_id',)
    list_display = ('additionalitem_id', 'aitm_item',
                    'aitm_itemdesc', 'aitm_cost',)

admin.site.register(Additionalitem, AdditionalitemAdmin)