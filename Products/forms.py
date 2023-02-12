from django.forms import ModelForm,TextInput
from .models import Products

class ProductAddForm(ModelForm):
    class Meta:
        model = Products
        fields = ["Product_Name","Brand","Category","Discription","Price","Stock","Shop_Name","Image"]
        widgets = {
            "Price":TextInput(attrs={"type":"number"}),
            "Stock":TextInput(attrs={"type":"Number"}),
        }