#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from principal.models import Fotos

class FotosForm(ModelForm):
    class Meta:
        model = Fotos