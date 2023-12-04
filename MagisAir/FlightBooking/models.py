from django.db import models

# Create your models here.
class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    pax_lname = models.CharField(max_length=255)
    pax_fname = models.CharField(max_length=255)
    pax_birthdate = models.DateField()

    def __str__(self):
        return '{}'.format(self.passenger_id)

    class Meta:
        managed = False
        db_table = 'passenger'

class Booking(models.Model):
    bkg_passenger = models.OneToOneField('Passenger', models.DO_NOTHING, primary_key=True)
    bkg_flight = models.ForeignKey('FlightRoutes.Flight', models.DO_NOTHING, related_name='Flight')
    
    def get_passenger_ID(self):
        return '{}'.format(self.bkg_passenger)
    
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

    class Meta:
        managed = False
        db_table = 'additionalitem'

class BookingAdditionalitem(models.Model):
    bai_passenger = models.OneToOneField(Booking, models.DO_NOTHING, primary_key=True)
    bai_flight = models.ForeignKey(Booking, models.DO_NOTHING, related_name='+')
    bai_additionalitem = models.ForeignKey(Additionalitem, models.DO_NOTHING, 
                                            related_name='+')
    bai_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booking_additionalitem'
        unique_together = (('bai_passenger', 'bai_flight', 'bai_additionalitem'),)
