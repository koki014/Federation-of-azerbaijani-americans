from django.urls import path
from .views import (
    RegisterCreateView,
    RegisterDoneView,
    DonateView
)

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register"),
    path("congratulations/", RegisterDoneView.as_view(), name="register_done"),
    path("donante/", DonateView.as_view(), name='donate' )

]