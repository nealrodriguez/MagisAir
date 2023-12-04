from django.db import models

# Create your models here.
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

    def __str__(self):
        return '{}'.format(self.crew_id)

    class Meta:
        managed = False
        db_table = 'crew_member'

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    rle_title = models.CharField(max_length=255)
    rle_desc = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.role_id)

    class Meta:
        managed = False
        db_table = 'role'