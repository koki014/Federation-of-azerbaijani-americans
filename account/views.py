from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy
# from django.core.mail import send_mail

from django.views.generic import (
    CreateView,
    View
)
from .models import DonationUser
from .forms import RegisterForm


class RegisterCreateView(CreateView):
    model = DonationUser
    form_class = RegisterForm
    template_name = "registration.html"
    success_url = reverse_lazy('core:index')

    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user_email = user.email
    #     # print(user_obj, 'usero')
    #     send_mail('subject', 'body of the message', 'tech.academy.docker@gmail.com', [user_email,])
    #     form.save()
    #     print(user)

	
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     print(self.object)
    #     print(request.session['email'], 'user1')
    #     return super().post(request, *args, **kwargs)


