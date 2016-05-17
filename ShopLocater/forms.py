from django import forms
from django.forms import ModelForm
from .models import Task

class ShopForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'coordinatesx', 'coordinatesy',  'pictures' )
    
