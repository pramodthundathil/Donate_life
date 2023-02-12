from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    options = (
        ("Men","Men"),
        ("Women","Women"),
        ("Kid","Kid")
    )
    Product_Name = models.CharField(max_length=255)
    Brand = models.CharField(max_length=255)
    Category = models.CharField(max_length=20,choices=options)
    Discription = models.CharField(max_length=1000)
    Price = models.PositiveBigIntegerField()
    Stock = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Shop_Name = models.CharField(max_length=255)
    Image = models.ImageField(upload_to="product_image")
    Merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    status = models.BooleanField(default=False)

class ProductRequests(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    RequestedBy = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)