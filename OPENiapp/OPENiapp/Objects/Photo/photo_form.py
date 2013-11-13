from django import forms

class PhotoForm(forms.Form):
    path = forms.CharField()