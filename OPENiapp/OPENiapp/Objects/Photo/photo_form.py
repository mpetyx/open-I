from django import forms

class PhotoForm(forms.Form):
    """ Create the fields neseccary for the Post Photo page form """
    path = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Path/To/Photo'}))
    facebook = forms.BooleanField(required=False)
    twitter = forms.BooleanField(required=False)