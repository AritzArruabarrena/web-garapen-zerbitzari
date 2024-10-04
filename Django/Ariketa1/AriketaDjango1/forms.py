from django import forms
from .models import *


class IkasleForm(forms.ModelForm):
    class Meta:
        model=Ikasle
        fields=['izena','abizena','jaiotze_data']
        


class IkasgaiakForm(forms.ModelForm):
    class Meta:
        model=Ikasgaiak
        fields=['izena','maila','hizkuntza']
        
        

class NotakForm(forms.ModelForm):
    class Meta:
        model=Notak
        fields=['nota','oharra','ikasgai', 'ikasle']
        
        

class NotakEditatuForm(forms.ModelForm):
    class Meta:
        model=Notak
        fields=['nota','oharra','ikasgai', 'ikasle']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ikasgai'].disabled =True
        self.fields['ikasle'].disabled =True
        
