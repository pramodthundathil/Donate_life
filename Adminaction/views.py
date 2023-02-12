from django.shortcuts import render,redirect
from django.contrib.auth.models import Group,User
from Home.models import OrgDetails

def OrganisationApprovalReqestes(request):
    approvels = OrgDetails.objects.filter(activation_status = False)
    context = {
        'approvels':approvels
    }
    return render(request,"adminapprovels.html",context)

def OrganisationView(request,pk):
    org = OrgDetails.objects.filter(id = pk)
    context = {
        "org":org
    }
    return render(request,"vieworganisation.html",context)

def ApproveOrganisation(request,pk):
    org = OrgDetails.objects.get(id = pk)
    org.activation_status = True
    org.save()
    user = org.User
    user.is_active = True
    group = Group.objects.get(name="organisation")
    user.groups.add(group)
    user.save()
    return redirect("OrganisationView",pk = pk )

def Organisations(request):
    org = OrgDetails.objects.all()
    context = {
        "org":org
    }
    return render(request,'allorganisations.html',context)

def DeleteOrg(request,pk):
    org = OrgDetails.objects.get(id = pk)
    user = org.User
    user.delete()
    return redirect('Organisations')

def Donners(request):
    user = User.objects.filter(groups__name='donners')
    context = {
        "user":user
    }
    
    return render(request,'doners.html',context)