from .models import HousesModel
from django import forms
from django.forms import Textarea,TextInput,NumberInput

class HousesForm(forms.ModelForm):
    class Meta:
        model=HousesModel
        fields=["title","image","description","address","num_of_rooms","price","space"]
        
        widgets={
            'title':TextInput(attrs={
                'class':'form-control',
                'name':'title',
                'placeholder':'Title'
            }),
            'description':Textarea(attrs={
                'class':'form-control',
                'name':'description',
                'placeholder':'Description',
                'cols':20,
                'rows':20
            }),
            'address':TextInput(attrs={
                'class':'form-control',
                'name':'address',
                'placeholder':'Address'
            }),
            'num_of_rooms':NumberInput(attrs={
                'class':'form-control',
                'name':'num_of_rooms',
                'placeholder':'Number of rooms'
            }),
            'price':NumberInput(attrs={
                'class':'form-control',
                'name':'price',
                'placeholder':'Price'
            }),
            'space':NumberInput(attrs={
                'class':'form-control',
                'name':'space',
                'placeholder':'Space'
            }),
        }