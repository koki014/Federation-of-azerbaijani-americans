
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from django.views.generic import (
    CreateView,
    TemplateView,
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


# class DonateView(TemplateView):
#     form_class = SignUpForm
#     template_name='donate1.html'


    
class DonateView(TemplateView):
    form_class = SignUpForm
    template_name='donate1.html'

    def get(self, request):
        form = SignUpForm()

        context = {'form': form}
        return render(request, self.template_name, context)


    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            # form.save()
            membership_id = request.POST.get('membership_id')
            user = DonationUser.objects.filter(membership_id=membership_id).first()
            if not user:
                return redirect('/')
            # text = form.cleaned_data['post']
            # form = SensorForm()
            return redirect('account:profile')

        context = {'form': form}
        return render(request, self.template_name, context)



    # def get(self, request):
    #     form = SignUpForm()
    #     return render(request, 'index.html', {"form": form})


class DonationUserDetailView(DetailView):
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         print(form)
#         if form.is_valid():
#             user = form.save()
#             membership_id = form.clean_data['membership_id']
#             user = authenticate(request, membership_id=user.membership_id)
#             if user is not None:
#                 login(request, user)
#             else:
#                 print("user is not authenticated")
#             return redirect('users:profile')
#     else:
#         form = SignUpForm()
#     return render(request, 'donate1.html', {'form': form})