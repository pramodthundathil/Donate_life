from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm,Textarea,TextInput,PasswordInput,CharField
from .models import OrgDetails


class UserAddForm(UserCreationForm):
    
   
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-input','placeholder':'Password'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-input','placeholder':'Password confirm'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-input','placeholder':'User Name'}),
            'first_name': TextInput(attrs={'class': 'form-input','placeholder':'First Name'}),
            'last_name': TextInput(attrs={'class': 'form-input','placeholder':'Last Name'}),
            'email': TextInput(attrs={'class': 'form-input','placeholder':'Email Id'})  

        }
        
class OrgDetailForm(ModelForm):
    class Meta:
        model = OrgDetails
        fields = ["Organasation_Name","Organasation_Type","Phone_Number","Place","Contry","Address","Registration_Number","Number_of_members","Date_of_Registration","Registration_Document"]
        widgets = {
            "Phone_Number":TextInput(attrs={"type":'number'}),
            "Number_of_members":TextInput(attrs={"type":"number"}),
            "Date_of_Registration":TextInput(attrs={"type":"date"})
        }