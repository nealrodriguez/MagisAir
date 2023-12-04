from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

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

class PassengerCreateView(CreateView):
    model = Passenger
    fields = '__all__'
    template_name = 'FlightBooking/passengersCreate.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = '__all__'
    template_name = 'FlightBooking/bookingsCreate.html'

class AdditionalitemCreateView(CreateView):
    model = Additionalitem
    fields = '__all__'
    template_name = 'FlightBooking/additionalitemsCreate.html'

class BookingAdditionalitemCreateView(CreateView):
    model = BookingAdditionalitem
    fields = '__all__'
    template_name = 'FlightBooking/bookingAddItemsCreate.html'

class PassengerDetailview(DetailView):
    model = Passenger
    template_name = 'FlightBooking/successfullyAdded.html'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'FlightBooking/successfullyAdded.html'

class AdditionalitemDetailview(DetailView):
    model = Additionalitem
    template_name = 'FlightBooking/successfullyAdded.html'

class BookingAdditionalitemDetailview(DetailView):
    model = BookingAdditionalitem
    template_name = 'FlightBooking/successfullyAdded.html'