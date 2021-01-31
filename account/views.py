
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
)
from django.views.generic.detail import DetailView
from .models import DonationUser
from .forms import RegisterForm, SignUpForm



class RegisterCreateView(CreateView):
    model = DonationUser
    form_class = RegisterForm
    template_name = "registration.html"
    success_url = reverse_lazy('account:register_done') 


class RegisterDoneView(TemplateView):
    template_name = 'congratulation.html'


class DonateView(TemplateView):
    form_class = SignUpForm
    template_name='donate.html'


    def get(self, request):
        form = SignUpForm()

        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            membership_id = request.POST.get('membership_id')
            user = DonationUser.objects.filter(membership_id=membership_id).first()
            if not user:
                return redirect('account:donate')
            return redirect(user.get_absolute_url())
        context = {'form': form}
        return render(request, self.template_name, context)





class DonationUserDetailView(DetailView):
    model = DonationUser
    template_name = 'profile.html'
    context_object_name = 'user_object'

    def get_object(self):
        return get_object_or_404(DonationUser, membership_id=self.kwargs.get('membership_id'))

    def get_context_data(self, **kwargs):
        context = super(DonationUserDetailView, self).get_context_data(**kwargs)
        return context  
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = DonationUser.objects.filter(membership_id=membership_id).first()
    #     return context
    
