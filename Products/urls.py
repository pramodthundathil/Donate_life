from django.urls import path 
from .import views

urlpatterns = [
    path("AddProducts",views.AddProducts,name="AddProducts"),
    path("RequestProduct/<int:pk>",views.RequestProduct,name="RequestProduct"),
    path("RequestedProducts",views.RequestedProducts,name="RequestedProducts"),
    path("ApprovedProducts",views.ApprovedProducts,name="ApprovedProducts"),
    path("CancelRequest/<int:pk>",views.CancelRequest,name="CancelRequest"),
    path("DonerVviewProductRequests",views.DonerVviewProductRequests,name="DonerVviewProductRequests"),
    path("ViewRequest/<int:pk>",views.ViewRequest,name="ViewRequest"),
    path("MyProducts",views.MyProducts,name="MyProducts"),
    path("DeleteProduct/<int:pk>",views.DeleteProduct,name="DeleteProduct"),
    path("DonerViewAprovedProducts",views.DonerViewAprovedProducts,name="DonerViewAprovedProducts"),
    path("ApproveRequest/<int:pk>",views.ApproveRequest,name="ApproveRequest")
]
