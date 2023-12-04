from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Passenger, Booking, Additionalitem, BookingAdditionalitem

class PassengerListView(ListView):
    model = Passenger
    def get(self, request):
        passengers = Passenger.objects.all()
        return render(request, 'FlightBooking/passengers.html', {
            'passengers': passengers
        })

class BookingListView(ListView):
    model = Booking
    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, 'FlightBooking/bookings.html', {
            'bookings': bookings
        })

class AdditionalitemListView(ListView):
    model = Additionalitem
    def get(self, request):
        additionalItems = Additionalitem.objects.all()
        return render(request, 'FlightBooking/additionalItems.html', {
            'additionalItems': additionalItems
        })

class BookingAdditionalitemListView(ListView):
    model = BookingAdditionalitem
    def get(self, request):
        bookingAddItems = BookingAdditionalitem.objects.all()
        return render(request, 'FlightBooking/bookingAddItems.html', {
            'bookingAddItems': bookingAddItems
        })