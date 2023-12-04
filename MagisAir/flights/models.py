# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Additionalitem(models.Model):
    additionalitem_id = models.AutoField(primary_key=True)
    aitm_item = models.CharField(max_length=255)
    aitm_itemdesc = models.CharField(max_length=255, blank=True, null=True)
    aitm_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'additionalitem'

class Booking(models.Model):
    bkg_passenger = models.OneToOneField('Passenger', models.DO_NOTHING, primary_key=True)
    bkg_flight = models.ForeignKey('Flight', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'booking'
        unique_together = (('bkg_passenger', 'bkg_flight'),)


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

class CrewAssignment(models.Model):
    cas_crew_id = models.IntegerField(primary_key=True)
    cas_flight_id = models.CharField(max_length=10)
    cas_role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crew_assignment'
        unique_together = (('cas_crew_id', 'cas_flight_id', 'cas_role_id'),)

class CrewMember(models.Model):
    crew_id = models.AutoField(primary_key=True)
    crw_lname = models.CharField(max_length=255)
    crw_fname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'crew_member'

class Flight(models.Model):
    flight_id = models.CharField(primary_key=True, max_length=10)
    flt_route = models.ForeignKey('Route', models.DO_NOTHING, related_name='+')
    flt_datetime_departure = models.DateTimeField()
    flt_datetime_arrival = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'flight'


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    loc_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'location'


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    pax_lname = models.CharField(max_length=255)
    pax_fname = models.CharField(max_length=255)
    pax_birthdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'passenger'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    rle_title = models.CharField(max_length=255)
    rle_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    rt_origin = models.ForeignKey(Location, models.DO_NOTHING, db_column='rt_origin', related_name='+')
    rt_destination = models.ForeignKey(Location, models.DO_NOTHING, db_column='rt_destination')
    rt_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'
