from turtle import title
from django import forms
from django.forms import ModelForm
from .models import Blouses

class Blousesform(ModelForm):
    title=forms.TextInput()
    description = forms.Textarea()
    image=forms.ImageField()

    class Meta:
        model=Blouses
        fields = ['title','description','image']

