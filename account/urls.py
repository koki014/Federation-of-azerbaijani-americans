from django.urls import path
from .views import (
    RegisterCreateView,
)

app_name = 'account'

urlpatterns = [
    path("register/", RegisterCreateView.as_view(), name="register"),
]