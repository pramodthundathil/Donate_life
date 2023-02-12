from django.shortcuts import render,redirect
from .models import Products,ProductRequests
from Home.models import OrgDetails
from .forms import ProductAddForm
from django.contrib import messages

def AddProducts(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.Merchant = request.user
            product.save()
            messages.info(request,"Product Saved")
            return redirect('AddProducts')
    context = {
        "form":form
    }
    return render(request,"addproducts.html",context)

def MyProducts(request):
    product = Products.objects.filter(Merchant = request.user)
    context = {
        "product":product
    }
    return render(request,"myproducts.html",context)

def DeleteProduct(request,pk):
    prod = Products.objects.get(id = pk)
    prod.Image.delete()
    prod.delete()
    messages.info(request,"Product deleted")
    return redirect('MyProducts')

def RequestProduct(request,pk):
    product = Products.objects.get(id = pk)
    requests = ProductRequests.objects.create(product = product,RequestedBy = request.user)
    requests.save()
    return redirect("OrganasationHome")

def RequestedProducts(request):
    req = ProductRequests.objects.filter(RequestedBy = request.user,status = False)
    context = {
        'req':req
    }
    return render(request,"productrequests.html",context)

def CancelRequest(request,pk):
    req = ProductRequests.objects.get(id = pk)
    req.delete()
    return redirect('RequestedProducts')

def ApprovedProducts(request):
    req = ProductRequests.objects.filter(RequestedBy = request.user,status=True)
    context = {
        'req':req
    }
    return render(request,"approvedproducts.html",context)

def DonerVviewProductRequests(request):
    product = Products.objects.filter(Merchant = request.user)
    req = ProductRequests.objects.filter(status=False)
    context = {
        'req':req,
        'dis':"Organisation Product Request"
    }
     
    return render(request,'productrequestdonnerview.html',context)

def ViewRequest(request,pk):
    req = ProductRequests.objects.filter(id = pk)
    requ = ProductRequests.objects.get(id = pk)
    org = OrgDetails.objects.filter(User = requ.RequestedBy)
    
    context = {
        "req":req,
        'org':org
    }
    return render(request,"viewrequest.html",context)

def DonerViewAprovedProducts(request):
    req = ProductRequests.objects.filter(status=True)
    context = {
        'req':req,
        'dis':"Donated Product List"
    }
    return render(request,'productrequestdonnerview.html',context)

def ApproveRequest(request,pk):
    req = ProductRequests.objects.get(id = pk)
    prod = req.product
    prod.status = True
    prod.save()
    req.status = True
    req.save()
    messages.info(request,"Product Donated") 
    return redirect('DonerViewAprovedProducts')

