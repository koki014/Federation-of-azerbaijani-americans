from django.urls import reverse_lazy


from django.views.generic import (
    CreateView,
    TemplateView
)
from .models import DonationUser
from .forms import RegisterForm


class RegisterCreateView(CreateView):
    model = DonationUser
    form_class = RegisterForm
    template_name = "registration.html"
    success_url = reverse_lazy('account:register_done') 


class RegisterDoneView(TemplateView):
    template_name = 'congratulation.html'


class DonateView(TemplateView):
    template_name='donate1.html'
