from django.urls import path

from. views import (AdditionalitemListView, BookingAdditionalitemListView,
                    BookingListView, PassengerListView)

urlpatterns = [
    path('passengers', PassengerListView.as_view(), name='passenger-table'),
    path('bookings', BookingListView.as_view(), name='booking-table'),
    path('addItems', AdditionalitemListView.as_view(), name='addItem-table'),
    path('bookingAddItems', BookingAdditionalitemListView.as_view(), name='bookingAddItem-table')
]

app_name='FlightBooking'