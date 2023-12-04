from django.urls import path

from. views import (CrewMemberListView, CrewRoleListView,
                    CrewAssignmentListView, CrewAssignmentCreateView,
                    CrewAssignmentDetailView, CrewRoleCreateView,
                    CrewRoleDetailView, CrewMemberCreateView,
                    CrewMemberDetailView)

urlpatterns = [
    path('members', CrewMemberListView.as_view(), name='crewMember-table'),
    path('roles', CrewRoleListView.as_view(), name='crewRole-table'),
    path('assignments', CrewAssignmentListView.as_view(), name='crewAssignment-table'),
    path('members/add', CrewMemberCreateView.as_view(), name='crewMember-add'),
    path('roles/add', CrewRoleCreateView.as_view(), name='crewRole-add'),
    path('assignments/add', CrewAssignmentCreateView.as_view(), name='crewAssignment-add'),
    path('members/<pk>_added', CrewMemberDetailView.as_view(), name='added-member'),
    path('roles/<pk>_added', CrewRoleDetailView.as_view(), name='added-role'),
    path('assignments/<pk>_added', CrewAssignmentDetailView.as_view(), name='added-assignment')
]

app_name='CrewAssignments'