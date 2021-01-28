from django import forms
from django.forms import widgets
from .models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "full_name", 
            "email","birthday", 
            "phone_number", 
            "citizenship", 
            "education", 
            "current", 
            "permoment", 
            "member_of_ngo", 
            "usa_year", 
            "reasons", 
            "mention"
        )

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'name': 'fname',
                    'class': 'form-elements',
                    'placeholder': 'Name and Surname'
                }
            ),
            'birthday': forms.DateInput(
                attrs={
                    'name': 'dd',
                    'class': 'form-elements',
                    'placeholder': 'Date of Birth'
                }
            ),
            'email':  forms.EmailInput(
                attrs={
                    'name': 'email',
                    'class': 'form-elements',
                    'placeholder': 'E-mail address'
                }
            ),
            'phone_number' : forms.TextInput(
                attrs={
                    'name': 'phone',
                    'placeholder': 'Phone Number',
                    'class': 'form-elements', 
                    }
            ),
            'citizenship': forms.TextInput(
                attrs={
                    'name': 'citizen',
                    'class': 'form-elements',
                    'placeholder': 'Citizenship'
                }
            ),
            'education': forms.TextInput(
                attrs={
                    'name': 'edu',
                    'class': 'form-elements',
                    'placeholder': 'Education'
                }
            ),
            'current': forms.TextInput(
                attrs={
                    'name': 'employe',
                    'class': 'form-elements',
                    'placeholder': 'Current employer and Position'
                }
            ),
            'permoment': forms.TextInput(
                attrs={
                    'name': 'permoment',
                    'class': 'form-elements',
                    'placeholder': 'Permament/Mailing adress'
                }
            ),
            'member_of_ngo': forms.TextInput(
                attrs={
                    'name': 'member',
                    'class': 'form-elements',
                    'placeholder': 'Member of other NGOs or Associations'
                }
            ),
            'member_of_ngo': forms.Textarea(
                attrs={
                    'name': 'member',
                    'class': 'form-elements',
                    'placeholder': 'Member of other NGOs or Associations'
                }
            ),
            'usa_year': forms.NumberInput(
                attrs={
                    'name': 'year',
                    'class': 'form-elements',
                    'placeholder': 'The year move to USA'
                }
            ),
            'reasons': forms.Textarea(
                attrs={
                    'name': '',
                    'class': 'form-elements',
                    'placeholder': 'Please mention the reasons why you wish to join FAA and your expectation from organization'
                }
            ),
            'mention': forms.Textarea(
                attrs={
                    'name': '',
                    'class': 'form-elements',
                    'placeholder': 'Please mention the way you are willing to contribute with FAA'
                }
            ),

        }



