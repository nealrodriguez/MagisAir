from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_id = models.CharField(primary_key=True, max_length=10)
    flt_route = models.ForeignKey('FlightRoutes.Route', models.DO_NOTHING, related_name='route')
    flt_datetime_departure = models.DateTimeField()
    flt_datetime_arrival = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.flight_id)

    class Meta:
        managed = False
        db_table = 'flight'

class CrewMember(models.Model):
    crew_id = models.AutoField(primary_key=True)
    crw_lname = models.CharField(max_length=255)
    crw_fname = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.crew_id)
    
    def get_absolute_url(self):
        return reverse('CrewAssignments:added-member', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'crew_member'

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    rle_title = models.CharField(max_length=255)
    rle_desc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.role_id)
    
    def get_absolute_url(self):
        return reverse('CrewAssignments:added-role', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'role'

class CrewAssignment(models.Model):
    cas_crew_id = models.OneToOneField('CrewMember', models.DO_NOTHING,related_name='+')
    cas_flight_id = models.ForeignKey('Flight', models.DO_NOTHING, related_name='+')
    cas_role_id = models.ForeignKey('Role', models.DO_NOTHING, related_name='+')

    def get_absolute_url(self):
        return reverse('CrewAssignments:added-assignment', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'crew_assignment'
        unique_together = (('cas_crew_id', 'cas_flight_id', 'cas_role_id'),)