from django import forms

class SignUp(forms.Form):
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    Email = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=30)