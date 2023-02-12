from django.urls import path
from .import views

urlpatterns = [
    path("OrganisationApprovalReqestes",views.OrganisationApprovalReqestes,name="OrganisationApprovalReqestes"),
    path("OrganisationView/<int:pk>",views.OrganisationView,name="OrganisationView"),
    path("ApproveOrganisation/<int:pk>",views.ApproveOrganisation,name="ApproveOrganisation"),
    path("Organisations",views.Organisations,name="Organisations"),
    path("DeleteOrg/<int:pk>",views.DeleteOrg,name="DeleteOrg"),
    path("Donners",views.Donners,name="Donners"),
]
