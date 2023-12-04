from django.contrib import admin
from .models import CrewAssignment, CrewMember, Role, Flight

class CrewAssignmentAdmin(admin.ModelAdmin):
    model = CrewAssignment
    search_fields = ('cas_crew_id', 'cas_flight_id',
                    'cas_role_id',)
    list_display = ('cas_crew_id', 'cas_flight_id',
                    'cas_role_id',)

class CrewMemberAdmin(admin.ModelAdmin):
    model = CrewMember
    search_fields = ('crew_id',)
    list_display = ('crew_id', 'crw_lname',
                    'crw_fname',)

class RoleAdmin(admin.ModelAdmin):
    model = Role
    search_fields = ('role_id',)
    list_display = ('role_id', 'rle_title', 
                    'rle_desc',)

admin.site.register(CrewAssignment, CrewAssignmentAdmin)
admin.site.register(CrewMember, CrewMemberAdmin)
admin.site.register(Role, RoleAdmin)