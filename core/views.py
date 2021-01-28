from core.models import Contact
from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from django.urls.base import reverse_lazy

from .forms import ContactForm, SubscriberForm


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'index.html'
    success_url = reverse_lazy('core:index')


class SubscriberView(CreateView):
    form_class = SubscriberForm
    template_name = 'index.html'
    success_url = reverse_lazy('core:index')