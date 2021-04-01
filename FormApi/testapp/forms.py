from django import forms

class StudentRegistation(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    passward = forms.CharField(widget=forms.PasswordInput)


