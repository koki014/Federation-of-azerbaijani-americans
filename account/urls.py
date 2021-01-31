from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    RegisterCreateView,
    RegisterDoneView,
    DonateView,
    # signup,
    DonationUserDetailView
)

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register"),
    path("congratulation/", RegisterDoneView.as_view(), name="register_done"),
    path("donate/", DonateView.as_view(), name='donate'),
    path('profile/(?P<membership_id>[-\w]+)//',  DonationUserDetailView.as_view(), name='profile'), 

]

