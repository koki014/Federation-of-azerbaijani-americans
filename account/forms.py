from django import forms
from django.forms import EmailInput
from .models import User


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("full_name", "email","birthday", "phone_number", "citizenship", "education", "current", "permoment", "member_of_ngo", "usa_year", "reasons")


