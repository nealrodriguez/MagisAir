from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

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