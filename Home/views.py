from django.shortcuts import redirect, render
from .forms import UserAddForm,OrgDetailForm
from django.contrib import messages
from django.contrib.auth.models import User,Group
from .decorators import admin_only
from django.contrib.auth import login,logout,authenticate
from .models import OrgDetails
from Products.models import Products




def homescreen(request):
    form = UserAddForm()
    return render(request,'index.html',{"forms":form})
@admin_only
def home(request):
    return render(request,'home.html')

def UserConfirm(request):
    return render(request,"usertypeconfirm.html")

def OrgRegister(request):
    form = OrgDetailForm()
    if request.method == "POST":
        form = OrgDetailForm(request.POST,request.FILES)
        if form.is_valid():
            org = form.save()
            org.User = request.user
            org.save()
            user = request.user
            user.is_active = False
            user.save()
            messages.info(request,"Your Request Is Submited Succesfully Please Wait for Approval")
            return redirect("signin")       
    context = {
        "form":form
    }
    return render(request,"organasationregister.html",context)

def OrganasationHome(request):
    product = Products.objects.all()
    context = {
        'product':product
    }
    return render(request,"organasationhome.html",context)

def DonnerConfirm(request):
    user = request.user
    group = Group.objects.get(name="donners")
    user.groups.add(group)
    user.save()
    return redirect('home')

def AdminHome(request):
    context = {
        "pendingorgcount":OrgDetails.objects.filter(activation_status = False).count(),
        'totalorgcount':OrgDetails.objects.filter(activation_status = True).count(),
        'donerscount':User.objects.filter(groups__name="donners").count()
        
    }
    return render(request,"adminhome.html",context)

def donate(request):
    return render(request,"donate.html")

def signup(request):
    
    if request.method =="POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('homescreen')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('homescreen')
            else:
                new_user = form.save()
                new_user.save()
                messages.info(request,"Account was Created")
                return redirect('homescreen')
            
    return redirect('homescreen')

def signin(request):
    
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('home')
        
        else:
            messages.info(request,'Username or Password Incorrect or Your Activation Request is Not Yet Approved Please Contact Administrator')
            return redirect('homescreen')
    
    return redirect('homescreen')

def signout(request):
    logout(request)
    return redirect('homescreen')
    
            
            
        

    