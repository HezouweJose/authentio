# forms.py
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname']  # Ajoutez d'autres champs d'utilisateur selon vos besoins

class UserAuthenticationForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    # Ajoutez d'autres champs d'authentification selon vos besoins
