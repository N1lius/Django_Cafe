from django import forms

class UserForm(forms.Form):
 name = forms.CharField(label="Марка машины",
    widget=forms.TextInput(attrs={"class": "myfield"}))
 age = forms.IntegerField(label="Год выпуска",
    widget=forms.NumberInput(attrs={"class": "myfield"}))
