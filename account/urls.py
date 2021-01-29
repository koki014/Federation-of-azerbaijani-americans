from django.urls import path
from .views import (
    RegisterCreateView,
    RegisterDoneView,
    DonateView
)

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register"),
    path("congratulation/", RegisterDoneView.as_view(), name="register_done"),
    path("donate/", DonateView.as_view(), name='donate' )

]