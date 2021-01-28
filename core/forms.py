from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Contact, Subscriber


class ContactForm(forms.ModelForm):

    class Meta:
            model = Contact
            fields = (
                'name',
                'email',
                'message',  
            )

            widgets = {
                
                'name': forms.TextInput(attrs={
                    'class': 'form-control col-6',
                    'placeholder': 'Your Name *'
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control col-6',
                    'placeholder': 'Your Email *'
                }),
                'message': forms.Textarea(attrs={
                    'class': 'form-control col-12',
                    'placeholder': 'Your Message'
                }),
                
            }

class SubscriberForm(forms.Form):
    mail = forms.EmailField(max_length=125, widget=forms.EmailInput(attrs={
        'class': 'form-control pl-3 shadow-none bg-transparent border-0', 
        'placeholder': 'Enter your email address'
    }), )

    class Meta:
        model = Subscriber
        fields = (
            'mail',
        )
