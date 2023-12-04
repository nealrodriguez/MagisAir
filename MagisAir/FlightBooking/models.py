from django.db import models

# Create your models here.
class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    pax_lname = models.CharField(max_length=255)
    pax_fname = models.CharField(max_length=255)
    pax_birthdate = models.DateField()

    def __str__(self):
        return '{}'.format(self.passenger_id)
    
    def get_absolute_url(self):
        return reverse('FlightBooking:added-passenger', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'passenger'

class Flight(models.Model):
    flight_id = models.CharField(primary_key=True, max_length=10)
    flt_route = models.ForeignKey('FlightRoutes.Route', models.DO_NOTHING, related_name='+')
    flt_datetime_departure = models.DateTimeField()
    flt_datetime_arrival = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.flight_id)

    class Meta:
        managed = False
        db_table = 'flight'

class Booking(models.Model):
    bkg_passenger = models.OneToOneField('Passenger', models.DO_NOTHING, primary_key=True)
    bkg_flight = models.ForeignKey('Flight', models.DO_NOTHING, related_name='Flight')

    def get_absolute_url(self):
        return reverse('FlightBooking:added-booking', kwargs={'pk': self.pk})
    
    class Meta:
        managed = False
        db_table = 'booking'
        unique_together = (('bkg_passenger', 'bkg_flight'),)

class Additionalitem(models.Model):
    additionalitem_id = models.AutoField(primary_key=True)
    aitm_item = models.CharField(max_length=255)
    aitm_itemdesc = models.CharField(max_length=255, blank=True, null=True)
    aitm_cost = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.additionalitem_id)
    
    def get_absolute_url(self):
        return reverse('FlightBooking:added-addItem', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'additionalitem'

class BookingAdditionalitem(models.Model):
    bai_passenger = models.OneToOneField('Passenger', models.DO_NOTHING, primary_key=True)
    bai_flight = models.ForeignKey('Flight', models.DO_NOTHING, related_name='+')
    bai_additionalitem = models.ForeignKey(Additionalitem, models.DO_NOTHING, 
                                            related_name='+')
    bai_quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.bai_passenger)
    
    def get_absolute_url(self):
        return reverse('FlightBooking:added-bookingAddItem', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'booking_additionalitem'
        unique_together = (('bai_passenger', 'bai_flight', 'bai_additionalitem'),)