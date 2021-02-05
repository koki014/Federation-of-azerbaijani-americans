
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.template import RequestContext
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    FormView,
)
from django.views.generic.edit import FormView
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



def payment_process(request, membership_id):

    # contextt = RequestContext(request)

    # user_object = DonationUser.objects.filter(membership_id=self.kwargs.get('membership_id'))
    # user_object = get_object_or_404(DonationUser, membership_id=self.kwargs.get('membership_id'))
    user_object = DonationUser.objects.get(membership_id=membership_id)
    print('salam')
    # if request.method == 'POST':
    amount = request.POST.get('amoun')
    print(amount)
    paypal_dict = {
        "business": "husubayli@gmail.com",
        "amount": "",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('core:index')),
        "return": request.build_absolute_uri(reverse('core:index')),
        "cancel_return": request.build_absolute_uri(reverse('core:index')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    
            # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "user_object": user_object}
    return render(request, "profile.html", context)




# class DonationUserDetailView(DetailView):
#     model = DonationUser
#     template_name = 'profile.html'
#     context_object_name = 'user_object'

#     def __init__(self):
#         request = self.request
#         self.paypal_dict = {
#             "business": "husubayli@gmail.com",
#             "amount": '10',
#             "item_name": "name of the item",
#             "invoice": "unique-invoice-id",
#             "notify_url": request.build_absolute_uri(reverse('core:index')),
#             "return": request.build_absolute_uri(reverse('core:index')),
#             "cancel_return": request.build_absolute_uri(reverse('core:index')),
#             "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#         }

#     def get_object(self):
#         return get_object_or_404(DonationUser, membership_id=self.kwargs.get('membership_id'))

#     def get_context_data(self, **kwargs):
#         context = super(DonationUserDetailView, self).get_context_data(**kwargs)
#         context['form'] =  PayPalPaymentsForm(initial=self.paypal_dict)
#         return context
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = DonationUser.objects.filter(membership_id=membership_id).first()
    #     return context
    
# class PaymentFormView(FormView):

# def payment_process(request):
#     amount = request.POST.get('amoun')
#     print(amount)
#     # What you want the button to do.
#     if request.method == 'POST':
#         paypal_dict = {
#             "business": "husubayli@gmail.com",
#             "amount": amount,
#             "item_name": "name of the item",
#             "invoice": "unique-invoice-id",
#             "notify_url": request.build_absolute_uri(reverse('core:index')),
#             "return": request.build_absolute_uri(reverse('core:index')),
#             "cancel_return": request.build_absolute_uri(reverse('core:index')),
#             "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#         }
#         # Create the instance.
#         form = PayPalPaymentsForm(initial=paypal_dict)
#         context = {"form": form}
#         return render(request, "payment.html", context)
