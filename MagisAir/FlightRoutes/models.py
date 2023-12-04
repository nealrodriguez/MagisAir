from django.db import models
from django.urls import reverse

# Create your models here.
class Flight(models.Model):
    flight_id = models.CharField(primary_key=True, max_length=10)
    flt_route = models.ForeignKey('Route', models.DO_NOTHING, related_name='+')
    flt_datetime_departure = models.DateTimeField()
    flt_datetime_arrival = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.flight_id)

    def get_absolute_url(self):
        return reverse('FlightRoutes:added-flight', kwargs={'pk': self.pk})
    
    class Meta:
        managed = False
        db_table = 'flight'

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    loc_name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.location_id)
    
    def get_absolute_url(self):
        return reverse('FlightRoutes:added-location', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'location'

class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    rt_origin = models.ForeignKey(Location, models.DO_NOTHING, db_column='rt_origin', related_name='+')
    rt_destination = models.ForeignKey(Location, models.DO_NOTHING, db_column='rt_destination')
    rt_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.route_id)
    
    def get_absolute_url(self):
        return reverse('FlightRoutes:added-route', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'route'