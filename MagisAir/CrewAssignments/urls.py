from django.urls import path

from. views import (CrewMemberListView, CrewRoleListView,
                    CrewAssignmentListView)

urlpatterns = [
    path('members', CrewMemberListView.as_view(), name='crewMember-table'),
    path('roles', CrewRoleListView.as_view(), name='crewRole-table'),
    path('assignments', CrewAssignmentListView.as_view(), name='crewAssignment-table')
]

app_name='CrewAssignments'