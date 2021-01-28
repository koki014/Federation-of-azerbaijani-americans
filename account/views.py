from django.utils.http import urlsafe_base64_decode
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    View
)
from .models import User
from .forms import RegisterForm

class RegisterCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "email/registration.html"
    success_url = reverse_lazy('account:login') 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        site_adres = self.request.is_secure() and "https://" or "http://" + self.request.META['HTTP_HOST']  # https://stackoverflow.com/
        send_confirmation_email(user, site_adres)

        return super().form_valid(form)



class UserActivate(View):

    def get(self, *args, **kwargs):
        uidb64 = kwargs.get('uidb64') 
        token = kwargs.get('token') 
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            success(self.request, 'Email is activeted')
            return redirect(reverse_lazy('account:login'))
        else:
            error(self.request, 'Email is not activeted')
            return redirect(reverse_lazy('account:register'))
