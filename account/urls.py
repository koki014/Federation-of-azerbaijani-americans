from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    RegisterCreateView,
    RegisterDoneView,
    DonateView,
    DonationUserUserDetailView
)

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register"),
    path('profile/',  login_required(DonationUserUserDetailView.as_view()), name='profile'),
    path("congratulation/", RegisterDoneView.as_view(), name="register_done"),
    path("donate/", DonateView.as_view(), name='donate' )

]

