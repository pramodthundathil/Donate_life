from django.db import models
from django.contrib.auth.models import User

class OrgDetails(models.Model):
    options = (
        ("Oldage Home","Oldage Home"),
        ("Orphenage","Orphanage"),
        ("Other","Other")
    )
    User = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Organasation_Name = models.CharField(max_length=255)
    Organasation_Type = models.CharField(max_length=255,choices=options)
    Phone_Number = models.IntegerField()
    Place = models.CharField(max_length=255)
    Contry = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Registration_Number = models.CharField(max_length=255)
    Number_of_members = models.IntegerField()
    Date_of_Registration = models.DateField(auto_now_add=False)
    Registration_Document = models.FileField(upload_to="Registration_documents")
    activation_status = models.BooleanField(default=False)
    
