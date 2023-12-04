from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import CrewAssignment, CrewMember, Role

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
    template_name = 'FlightBooking/membersCreate.html'

class CrewRoleCreateView(CreateView):
    model = Role
    fields = '__all__'
    template_name = 'FlightBooking/rolesCreate.html'

class CrewAssignmentCreateView(CreateView):
    model = CrewAssignment
    fields = '__all__'
    template_name = 'FlightBooking/assignmentsCreate.html'

class CrewMemberDetailView(DetailView):
    model = CrewMember
    template_name = 'FlightBooking/successfullyAdded.html'

class CrewRoleDetailView(DetailView):
    model = Role
    template_name = 'FlightBooking/successfullyAdded.html'

class CrewAssignmentDetailView(DetailView):
    model = CrewAssignment
    template_name = 'FlightBooking/successfullyAdded.html'