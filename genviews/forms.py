from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = ["title", "tagline", "price"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "Title"}),
            "tagline": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "Tagline"}),
            "price": forms.NumberInput(attrs={"class": "form-control form-control-sm", "placeholder": "Price (in ₹)"}),
        }


class ProductUpdateForm(forms.ModelForm):

    class Meta:

        model = Product
        fields = ["tagline", "price"]
        widgets = {
            "tagline": forms.TextInput(attrs={"class": "form-control form-control-sm", "placeholder": "Tagline"}),
            "price": forms.NumberInput(attrs={"class": "form-control form-control-sm", "placeholder": "Price (in ₹)"}),
        }
