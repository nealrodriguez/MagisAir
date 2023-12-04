from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import CrewAssignment, CrewMember, Role

def SQL_Query2(request):
    members = CrewMember.objects.raw("SELECT crew_id, CONCAT(crew_member.crw_lname, ', ', crew_member.crw_fname) AS Crew, role.rle_title AS Role, flight.flight_id AS Flight, location.loc_name AS Destination, flight.flt_datetime_departure AS Departure, flight.flt_datetime_arrival AS Arrival FROM crew_member, crew_assignment, role, flight, route, location WHERE crew_assignment.cas_crew_id = crew_member.crew_id AND crew_assignment.cas_role_id = role.role_id AND crew_assignment.cas_flight_id = flight.flight_id AND flight.flt_route_id = route.route_id AND route.rt_destination = location.location_id;")
    print(members)
    return render(request, 'CrewAssignments/SQL_Query2.html', {'data': members})

class CrewMemberListView(ListView):
    model = CrewMember
    def get(self, request):
        crewMembers = CrewMember.objects.all()
        return render(request, 'CrewAssignments/members.html', {
            'crewMembers': crewMembers
        })

class CrewRoleListView(ListView):
    model = Role
    def get(self, request):
        crewRoles = Role.objects.all()
        return render(request, 'CrewAssignments/roles.html', {
            'crewRoles': crewRoles
        })

class CrewAssignmentListView(ListView):
    model = CrewAssignment
    def get(self, request):
        crewAssignments = CrewAssignment.objects.all()
        return render(request, 'CrewAssignments/assignments.html', {
            'crewAssignments': crewAssignments
        })
    
class CrewMemberCreateView(CreateView):
    model = CrewMember
    fields = '__all__'
    template_name = 'CrewAssignments/membersCreate.html'

class CrewRoleCreateView(CreateView):
    model = Role
    fields = '__all__'
    template_name = 'CrewAssignments/rolesCreate.html'

class CrewAssignmentCreateView(CreateView):
    model = CrewAssignment
    fields = '__all__'
    template_name = 'CrewAssignments/assignmentsCreate.html'

class CrewMemberDetailView(DetailView):
    model = CrewMember
    template_name = 'CrewAssignments/successfullyAdded.html'

class CrewRoleDetailView(DetailView):
    model = Role
    template_name = 'CrewAssignments/successfullyAdded.html'

class CrewAssignmentDetailView(DetailView):
    model = CrewAssignment
    template_name = 'CrewAssignments/successfullyAdded.html'