from django.urls import path

from. views import (AdditionalitemListView, BookingAdditionalitemListView,
                    BookingListView, PassengerListView, AdditionalitemCreateView,
                    BookingAdditionalitemCreateView, BookingCreateView, PassengerCreateView,
                    AdditionalitemDetailview, BookingAdditionalitemDetailview, BookingDetailView,
                    PassengerDetailview)

urlpatterns = [
    path('passengers', PassengerListView.as_view(), name='passenger-table'),
    path('bookings', BookingListView.as_view(), name='booking-table'),
    path('addItems', AdditionalitemListView.as_view(), name='addItem-table'),
    path('bookingAddItems', BookingAdditionalitemListView.as_view(), name='bookingAddItem-table'),
    path('passengers/add', PassengerCreateView.as_view(), name='passenger-add'),
    path('bookings/add', BookingCreateView.as_view(), name='booking-add'),
    path('addItems/add', AdditionalitemCreateView.as_view(), name='addItem-add'),
    path('bookingAddItems/add', BookingAdditionalitemCreateView.as_view(), name='bookingAddItem-add'),
    path('passengers/<pk>_added', PassengerDetailview.as_view(), name='added-passenger'),
    path('bookings/<pk>_added', BookingDetailView.as_view(), name='added-booking'),
    path('addItems/<pk>_added', AdditionalitemDetailview.as_view(), name='added-addItem'),
    path('bookingAddItems/<pk>_added', BookingAdditionalitemDetailview.as_view, name='added-bookingAddItem')
]

app_name='FlightBooking'